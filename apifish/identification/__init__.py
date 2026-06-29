# -*- coding: utf-8 -*-

"""
The apifish.identification subpackage includes function to detect RNA spot in 2-d / 3-d and functions to segment or label
nuclei and cells.
"""

from .cluster_detection import detect_clusters
from .dense_decomposition import (
    decompose_dense,
    get_dense_region,
    simulate_gaussian_mixture,
)
from .spot_detection import (
    automated_threshold_setting,
    detect_spots,
    get_elbow_values,
    local_maximum_detection,
    spots_thresholding,
)
from .spot_modeling import (
    fit_subpixel,
    gaussian_2d,
    gaussian_3d,
    initialize_grid,
    modelize_spot,
    precompute_erf,
)
from .spot_utils import (
    build_reference_spot,
    compute_snr_spots,
    convert_spot_coordinates,
    get_breaking_point,
    get_object_radius_nm,
    get_object_radius_pixel,
    get_spot_surface,
    get_spot_volume,
)

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

from .cell_segmentation import (
    apply_unet_distance_double,
    apply_watershed,
    cell_watershed,
    from_distance_to_instances,
    get_watershed_relief,
    unet_distance_edge_double,
)
from .mask_postprocess import (
    clean_segmentation,
    label_instances,
    merge_labels,
    remove_disjoint,
)
from .mask_utils import (
    compute_mean_convexity_ratio,
    compute_mean_diameter,
    compute_surface_ratio,
    count_instances,
    thresholding,
)
from .nuc_segmentation import (
    apply_unet_3_classes,
    from_3_classes_to_instances,
    remove_segmented_nuc,
    unet_3_classes_nuc,
)

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
