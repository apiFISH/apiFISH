# -*- coding: utf-8 -*-

"""
The apifish.identification subpackage includes function to detect RNA spot in 2-d / 3-d and functions to segment or label
nuclei and cells.
"""

from .spot_detection import detect_spots
from .spot_detection import local_maximum_detection
from .spot_detection import spots_thresholding
from .spot_detection import automated_threshold_setting
from .spot_detection import get_elbow_values

from .dense_decomposition import decompose_dense
from .dense_decomposition import get_dense_region
from .dense_decomposition import simulate_gaussian_mixture

from .spot_modeling import modelize_spot
from .spot_modeling import initialize_grid
from .spot_modeling import gaussian_2d
from .spot_modeling import gaussian_3d
from .spot_modeling import precompute_erf
from .spot_modeling import fit_subpixel

from .cluster_detection import detect_clusters

from .spot_utils import convert_spot_coordinates
from .spot_utils import get_object_radius_pixel
from .spot_utils import get_object_radius_nm
from .spot_utils import build_reference_spot
from .spot_utils import get_spot_volume
from .spot_utils import get_spot_surface
from .spot_utils import compute_snr_spots
from .spot_utils import get_breaking_point


_spots = [
    "detect_spots",
    "local_maximum_detection",
    "spots_thresholding",
    "automated_threshold_setting",
    "get_elbow_values",
]

_dense = ["decompose_dense", "get_dense_region", "simulate_gaussian_mixture"]

_model = [
    "modelize_spot",
    "initialize_grid",
    "gaussian_2d",
    "gaussian_3d",
    "precompute_erf",
    "fit_subpixel",
]

_clusters = ["detect_clusters"]

_spot_utils = [
    "convert_spot_coordinates",
    "get_object_radius_pixel",
    "get_object_radius_nm",
    "build_reference_spot",
    "get_spot_volume",
    "get_spot_surface",
    "compute_snr_spots",
    "get_breaking_point",
]

from .cell_segmentation import unet_distance_edge_double
from .cell_segmentation import apply_unet_distance_double
from .cell_segmentation import from_distance_to_instances
from .cell_segmentation import cell_watershed
from .cell_segmentation import get_watershed_relief
from .cell_segmentation import apply_watershed

from .nuc_segmentation import unet_3_classes_nuc
from .nuc_segmentation import apply_unet_3_classes
from .nuc_segmentation import from_3_classes_to_instances
from .nuc_segmentation import remove_segmented_nuc

from .postprocess import label_instances
from .postprocess import merge_labels
from .postprocess import clean_segmentation
from .postprocess import remove_disjoint

from .mask_utils import thresholding
from .mask_utils import compute_mean_diameter
from .mask_utils import compute_mean_convexity_ratio
from .mask_utils import compute_surface_ratio
from .mask_utils import count_instances


_cell = [
    "unet_distance_edge_double",
    "apply_unet_distance_double",
    "from_distance_to_instances",
    "cell_watershed",
    "get_watershed_relief",
    "apply_watershed",
]

_nuc = [
    "unet_3_classes_nuc",
    "apply_unet_3_classes",
    "from_3_classes_to_instances",
    "remove_segmented_nuc",
]

_mask_postprocess = [
    "label_instances",
    "merge_labels",
    "clean_segmentation",
    "remove_disjoint",
]

_mask_utils = [
    "thresholding",
    "compute_mean_diameter",
    "compute_mean_convexity_ratio",
    "compute_surface_ratio",
    "count_instances",
]

__all__ = (
    _spots
    + _dense
    + _model
    + _clusters
    + _spot_utils
    + _cell
    + _nuc
    + _mask_postprocess
    + _mask_utils
)
