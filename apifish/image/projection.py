# -*- coding: utf-8 -*-

"""2-d projection functions."""

import numpy as np
import scipy.optimize as spo
from scipy.stats import sigmaclip
from skimage import filters
from skimage.util.shape import view_as_blocks
from tqdm import trange

from .quality import compute_focus
from ..formatting.utils import check_array, check_parameter

# ### Projections 2-d ###


def maximum_projection(image):
    """Project the z-dimension of an image, keeping the maximum intensity of
    each yx pixel.

    Parameters
    ----------
    image : np.ndarray
        A 3-d image with shape (z, y, x).

    Returns
    -------
    projected_image : np.ndarray
        A 2-d image with shape (y, x).

    """
    # check parameters
    check_array(
        image,
        ndim=3,
        dtype=[np.uint8, np.uint16, np.int32, np.int64, np.float32, np.float64],
    )

    # project image along the z axis
    projected_image = image.max(axis=0)

    return projected_image


def mean_projection(image, return_float=False):
    """Project the z-dimension of a image, computing the mean intensity of
    each yx pixel.

    Parameters
    ----------
    image : np.ndarray
        A 3-d tensor with shape (z, y, x).
    return_float : bool, default=False
        Return a (potentially more accurate) float array.

    Returns
    -------
    projected_image : np.ndarray
        A 2-d image with shape (y, x).

    """
    # check parameters
    check_array(
        image,
        ndim=3,
        dtype=[np.uint8, np.uint16, np.int32, np.int64, np.float32, np.float64],
    )

    # project image along the z axis
    if return_float:
        projected_image = image.mean(axis=0)
    else:
        projected_image = image.mean(axis=0).astype(image.dtype)

    return projected_image


def median_projection(image):
    """Project the z-dimension of a image, computing the median intensity of
    each yx pixel.

    Parameters
    ----------
    image : np.ndarray
        A 3-d image with shape (z, y, x).

    Returns
    -------
    projected_image : np.ndarray
        A 2-d image with shape (y, x).

    """
    # check parameters
    check_array(
        image,
        ndim=3,
        dtype=[np.uint8, np.uint16, np.int32, np.int64, np.float32, np.float64],
    )

    # project image along the z axis
    projected_image = np.median(image, axis=0)
    projected_image = projected_image.astype(image.dtype)

    return projected_image


def sum_projection(image):
    """Project the z-dimension of a image, computing the sum of each yx pixel.

    Parameters
    ----------
    image : np.ndarray
        A 3-d image with shape (z, y, x).

    Returns
    -------
    projected_image : np.ndarray
        A 2-d image with shape (y, x).

    """
    # check parameters
    check_array(
        image,
        ndim=3,
        dtype=[np.uint8, np.uint16, np.int32, np.int64, np.float32, np.float64],
    )

    # project image along the z axis
    projected_image = np.zeros((image.shape[1], image.shape[2]))
    for z_plan in image:
        projected_image += z_plan

    return projected_image


def focus_projection(image, proportion=0.75, neighborhood_size=7, method="median"):
    """Project the z-dimension of an image.

    Inspired from Samacoits Aubin's thesis (part 5.3, strategy 5). Compare to
    the original algorithm we use the same focus measures to select the
    in-focus z-slices and project our image.

    #. Compute a focus score for each pixel yx with a fixed neighborhood size.
    #. We keep a proportion of z-slices with the highest average focus score.
    #. Keep the median/maximum pixel intensity among the top 5 z-slices (at
       most) with the highest focus score.

    Parameters
    ----------
    image : np.ndarray
        A 3-d image with shape (z, y, x).
    proportion : float or int, default=0.75
        Proportion of z-slices to keep (float between 0 and 1) or number of
        z-slices to keep (positive integer).
    neighborhood_size : int or tuple or list, default=7
        The size of the square used to define the neighborhood of each pixel.
        An odd value is preferred. To define a rectangular neighborhood, a
        tuple or a list with two elements (height, width) can be provided.
    method : {`median`, `max`}, default=`median`
        Projection method applied on the selected pixel values.

    Returns
    -------
    projected_image : np.ndarray
        A 2-d image with shape (y, x).

    """
    # check parameters
    check_array(
        image,
        ndim=3,
        dtype=[np.uint8, np.uint16, np.int32, np.int64, np.float32, np.float64],
    )

    # compute focus measure for each pixel
    focus = compute_focus(image, neighborhood_size)

    # select and keep best z-slices
    indices_to_keep = get_in_focus_indices(focus, proportion)
    in_focus_image = image[indices_to_keep]
    focus = focus[indices_to_keep]

    # for each yx pixel, get the indices of the 5 best focus values
    top_focus_indices = np.argsort(focus, axis=0)
    n = min(focus.shape[0], 5)
    top_focus_indices = top_focus_indices[-n:, :, :]

    # build a binary matrix with the same shape of our in-focus image to keep
    # the top focus pixels only
    mask = [
        mask_
        for mask_ in map(
            lambda indices: _one_hot_3d(indices, depth=in_focus_image.shape[0]),
            top_focus_indices,
        )
    ]
    mask = np.sum(mask, axis=0, dtype=in_focus_image.dtype)

    # filter top focus pixels in our in-focus image
    in_focus_image = in_focus_image.astype(np.float64)
    in_focus_image[mask == 0] = np.nan

    # project image
    if method == "median":
        projected_image = np.nanmedian(in_focus_image, axis=0)
    elif method == "max":
        projected_image = np.nanmax(in_focus_image, axis=0)
    else:
        raise ValueError(
            "Parameter 'method' should be 'median' or 'max', not "
            "'{0}'.".format(method)
        )
    projected_image = projected_image.astype(image.dtype)

    return projected_image


def _one_hot_3d(indices, depth, return_boolean=False):
    """Build a 3-d one-hot matrix from a 2-d indices matrix.

    Parameters
    ----------
    indices : np.ndarray, int
        A 2-d tensor with integer indices and shape (y, x).
    depth : int
        Depth of the 3-d one-hot matrix.
    return_boolean : bool
        Return a boolean one-hot encoded matrix.

    Returns
    -------
    one_hot : np.ndarray
        A 3-d binary tensor with shape (depth, y, x)

    """
    # check parameters
    check_parameter(depth=int)
    check_array(
        indices,
        ndim=2,
        dtype=[
            np.uint8,
            np.uint16,
            np.uint32,
            np.uint64,
            np.int8,
            np.int16,
            np.int32,
            np.int64,
        ],
    )

    # initialize the 3-d one-hot matrix
    one_hot = np.zeros((indices.size, depth), dtype=indices.dtype)

    # flatten the matrix to easily one-hot encode it, then reshape it
    one_hot[np.arange(indices.size), indices.ravel()] = 1
    one_hot.shape = indices.shape + (depth,)

    # rearrange the axis
    one_hot = np.moveaxis(one_hot, source=2, destination=0)

    if return_boolean:
        one_hot = one_hot.astype(bool)

    return one_hot


# ### Slice selection ###


def in_focus_selection(image, focus, proportion):
    """Select and keep the 2-d slices with the highest level of focus.

    Helmli and Scherer’s mean method is used as a focus metric.

    Parameters
    ----------
    image : np.ndarray
        A 3-d tensor with shape (z, y, x).
    focus : np.ndarray, np.float64
        A 3-d tensor with a focus metric computed for each pixel of the
        original image. See :func:`apifish.stack.compute_focus`.
    proportion : float or int
        Proportion of z-slices to keep (float between 0 and 1) or number of
        z-slices to keep (positive integer).

    Returns
    -------
    in_focus_image : np.ndarray
        A 3-d tensor with shape (z_in_focus, y, x), with out-of-focus z-slice
        removed.

    """
    # check parameters
    check_array(
        image,
        ndim=3,
        dtype=[np.uint8, np.uint16, np.int32, np.int64, np.float32, np.float64],
    )

    # select and keep best z-slices
    indices_to_keep = get_in_focus_indices(focus, proportion)
    in_focus_image = image[indices_to_keep]

    return in_focus_image


def get_in_focus_indices(focus, proportion):
    """Select the best in-focus z-slices.

    Helmli and Scherer’s mean method is used as a focus metric.

    Parameters
    ----------
    focus : np.ndarray, np.float
        A 3-d tensor with a focus metric computed for each pixel of the
        original image. See :func:`apifish.stack.compute_focus`.
    proportion : float or int
        Proportion of z-slices to keep (float between 0 and 1) or number of
        z-slices to keep (positive integer).

    Returns
    -------
    indices_to_keep : List[int]
        Indices of slices with the best focus score.

    """
    # check parameters
    check_parameter(proportion=(float, int))
    check_array(focus, ndim=3, dtype=[np.float32, np.float64])
    if isinstance(proportion, float) and 0 <= proportion <= 1:
        n = int(focus.shape[0] * proportion)
    elif isinstance(proportion, int) and 0 <= proportion:
        n = int(proportion)
    else:
        raise ValueError(
            "'proportion' should be a float between 0 and 1 or a "
            "positive integer, but not {0}.".format(proportion)
        )

    # measure focus level per 2-d slices
    focus_levels = np.mean(focus, axis=(1, 2))

    # select the best z-slices
    n = min(n, focus_levels.size)
    indices_to_keep = list(np.argsort(-focus_levels)[:n])
    indices_to_keep = sorted(indices_to_keep)

    return indices_to_keep


# =============================================================================
# FOCAL PLANE INTERPOLATION
# =============================================================================


def reinterpolate_focal_plane(data, block_size_xy=256, window=10):
    """
    Reinterpolates the focal plane of a 3D image by breking it into blocks
    - Calculates the focal_plane and fwhm matrices by block
    - removes outliers
    - calculates the focal plane for each block using sigmaClip statistics
    - returns a tuple with focal plane and the range to use

    Parameters
    ----------
    data : numpy array
        input 3D image.
    block_size_xy : int
        size of blocks in XY, typically 256.
    window : int, optional
        number of planes before and after the focal plane to construct the z_range. The default is 0.

    Returns
    -------
    focal_plane_matrix : numpy array
        focal plane matrix.
    z_range : tuple
        focus_plane, z_range.
    block : numpy array
        block representation of 3D image.

    """

    # breaks into subplanes, iterates over them and calculates the focal_plane in each subplane.
    focal_plane_matrix, _, block = calculate_focus_per_block(
        data, block_size_xy=block_size_xy
    )
    focal_planes_to_process = focal_plane_matrix[~np.isnan(focal_plane_matrix)]

    focal_plane, _, _ = sigmaclip(focal_planes_to_process, high=3, low=3)
    focus_plane = np.mean(focal_plane)
    if np.isnan(focus_plane):
        # focus_plane detection failed. Using full stack.
        focus_plane = data.shape[0] // 2
        z_range = focus_plane, range(0, data.shape[0])
    else:
        focus_plane = np.mean(focal_plane).astype("int64")
        zmin = np.max([focus_plane - window, 0])
        zmax = np.min([focus_plane + window, data.shape[0]])
        z_range = focus_plane, range(zmin, zmax)

    return focal_plane_matrix, z_range, block


def calculate_focus_per_block(data, block_size_xy=128):
    """
    Calculates the most likely focal plane of an image by breaking into blocks and calculating
    the focal plane in each block

    - breaks image into blocks
    - returns the focal plane + fwhm for each block

    Parameters
    ----------
    data : TYPE
        DESCRIPTION.
    block_size_xy : TYPE, optional
        DESCRIPTION. The default is 512.

    Returns
    -------
    focal_plane_matrix: np array
        matrix containing the maximum of the laplacian variance per block
    fwhm: np array
        matrix containing the fwhm of the laplacian variance per block
    block: np array
        3D block reconstruction of matrix
    """

    n_planes = data.shape[0]
    block_size = (n_planes, block_size_xy, block_size_xy)
    block = view_as_blocks(data, block_size).squeeze()
    focal_plane_matrix = np.zeros(block.shape[0:2])
    fwhm = {}

    for i in trange(block.shape[0]):
        for j in range(block.shape[1]):
            focal_plane_matrix[i, j], fwhm[i, j] = find_focal_plane(block[i, j])

    return focal_plane_matrix, fwhm, block


def find_focal_plane(data, threshold_fwhm=20):
    """
    This function will find the focal plane of a 3D image
    - calculates the laplacian variance of the image for each z plane
    - fits 1D gaussian profile on the laplacian variance
    - to get the maximum (focal plane) and the full width at half maximum
    - it returns nan if the fwhm > threshold_fwhm (means fit did not converge)
    - threshold_fwhm should represend the width of the laplacian variance curve
    - which is often 5-10 planes depending on sample.

    Parameters
    ----------
    data : numpy array
        input 3D image ZYX.
    threshold_fwhm : float, optional
        threshold fwhm used to remove outliers. The default is 20.

    Returns
    -------
    focal_plane : float
        focal plane: max of fitted z-profile.
    fwhm : float
        full width hald maximum of fitted z-profile.

    """
    # finds focal plane
    raw_images = [data[i, :, :] for i in range(data.shape[0])]
    laplacian_variance = [np.var(filters.laplace(img)) for img in raw_images]
    laplacian_variance = laplacian_variance / max(laplacian_variance)
    x_coord = range(len(laplacian_variance))
    fit_result = fit_1d_gaussian_scipy(
        x_coord,
        laplacian_variance,
        title="laplacian variance z-profile",
    )

    if len(fit_result) > 0:
        focal_plane = fit_result["gauss1d.pos"]
        fwhm = fit_result["gauss1d.fwhm"]

        if fwhm > threshold_fwhm:
            fwhm, focal_plane = np.nan, np.nan
    else:
        fwhm, focal_plane = np.nan, np.nan

    return focal_plane, fwhm


# Gaussian function
# @jit(nopython=True)
def gaussian(x, a=1, mean=0, std=0.5):
    return (
        a
        * (1 / (std * (np.sqrt(2 * np.pi))))
        * (np.exp(-((x - mean) ** 2) / ((2 * std) ** 2)))
    )


def fit_1d_gaussian_scipy(x, y, title=""):
    """
    Fits a function using a 1D Gaussian and returns parameters if successfull.
    Otherwise will return an empty dict
    Uses scipy spo package

    Parameters
    ----------
    x : numpy 1D array
        x data.
    y : numpy 1D array
        y data.
    title : str, optional
        figure title. The default is ''.

    Returns
    -------
    {}
        dictionary with fitting parameters.

    """
    fit_result = {}

    try:
        fitgauss = spo.curve_fit(gaussian, x, y)
        fit_result["gauss1d.pos"] = fitgauss[0][1]
        fit_result["gauss1d.ampl"] = fitgauss[0][0]
        fit_result["gauss1d.fwhm"] = 2.355 * fitgauss[0][2]
    except RuntimeError:
        return {}
    except ValueError:
        fit_result["gauss1d.pos"] = np.mean(x)
        fit_result["gauss1d.ampl"] = 0.0
        fit_result["gauss1d.fwhm"] = 0.0
        # Returned middle plane
        return fit_result

    return fit_result


def reassemble_images(focal_plane_matrix, block, window=0):
    """
    Makes 2D image from 3D stack by reassembling sub-blocks
    For each sub-block we know the optimal focal plane, which is
    selected for the assembly of the while image

    Parameters
    ----------
    focal_plane_matrix : numpy 2D array
        matrix containing the focal plane selected for each block.
    block : numpy matrix
        original 3D image sorted by blocks.

    Returns
    -------
    output : numpy 2D array
        output 2D projection

    """

    # Fix ValueError: cannot convert float NaN to integer
    focal_plane_matrix = np.nan_to_num(focal_plane_matrix)
    # gets image size from block image
    number_blocks = block.shape[0]
    block_size_xy = block.shape[3]
    im_size = number_blocks * block_size_xy

    # gets ranges for slicing
    slice_coordinates = [
        range(x * block_size_xy, (x + 1) * block_size_xy) for x in range(number_blocks)
    ]

    # creates output image
    output = np.zeros((im_size, im_size))

    # gets more common plane
    focal_planes = []
    for i, i_slice in enumerate(slice_coordinates):
        for j, j_slice in enumerate(slice_coordinates):
            focal_planes.append(int(focal_plane_matrix[i, j]))
    most_common_focal_plane = max(set(focal_planes), key=focal_planes.count)

    # reassembles image
    if window == 0:
        # takes one plane block
        for i, i_slice in enumerate(slice_coordinates):
            for j, j_slice in enumerate(slice_coordinates):
                focus = int(focal_plane_matrix[i, j])
                if np.abs(focus - most_common_focal_plane) > 1:
                    focus = int(most_common_focal_plane)
                output[i_slice[0] : i_slice[-1] + 1, j_slice[0] : j_slice[-1] + 1] = (
                    block[i, j][focus, :, :]
                )
    else:
        # takes neighboring planes by projecting
        for i, i_slice in enumerate(slice_coordinates):
            for j, j_slice in enumerate(slice_coordinates):
                focus = int(focal_plane_matrix[i, j])
                if np.abs(focus - most_common_focal_plane) > 1:
                    focus = int(most_common_focal_plane)
                zmin = np.max((0, focus - round(window / 2)))
                zmax = np.min((block[i, j].shape[0], focus + round(window / 2)))
                block_img = block[i, j][:, :, :]
                output[i_slice[0] : i_slice[-1] + 1, j_slice[0] : j_slice[-1] + 1] = (
                    maximum_projection(block_img[zmin:zmax])
                )

    return output
