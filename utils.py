import sys
from contextlib import contextmanager
from typing import Tuple, List, Sequence
from pathlib import Path

ALL_CATEGORIES = (
    "bottle", 
    "cable", 
    "capsule", 
    "carpet", 
    "grid", 
    "hazelnut", 
    "leather", 
    "metal_nut", 
    "pill", 
    "screw", 
    "tile", 
    "toothbrush", 
    "transistor",
    "wood",
    "zipper"
)

@contextmanager
def commandline_args(*args):
    old_argv = list(sys.argv)
    sys.argv.clear()
    sys.argv.extend(args)
    
    yield

    sys.argv.clear()
    sys.argv.extend(old_argv)

def get_train_args(
    exp_name: str,
    dst_folders: Tuple[str, str], # folder, subfolder
    categories: Tuple[str],
    backbone: str = "wideresnet50", 
    patchsize: int = 3, 
    image_size: int = 224, # for center-crop 
    resize: int = 256, # final image size
    sampler_percentage: float= 0.001,
    target_embed_dimension: int = 1024,
    anomaly_scorer_num_nn: int = 1,
) -> List[str]:
    args = [
        "command",
        "--seed",
        "0",
        "--save_patchcore_model",
        "--log_group",
        exp_name,
        "--log_project",
        dst_folders[1],
        dst_folders[0],
        "patch_core",
        "-b",
        backbone,
        "-le",
        "layer2",
        "-le",
        "layer3",
        "--pretrain_embed_dimension",
        "1024",
        "--target_embed_dimension",
        f"{target_embed_dimension}",
        "--anomaly_scorer_num_nn",
        f"{anomaly_scorer_num_nn}",
        "--patchsize",
        f"{patchsize}",
        "sampler",
        "-p",
        f"{sampler_percentage}",
        "approx_greedy_coreset",
        "dataset",
        "--resize",
        f"{resize}",
        "--imagesize",
        f"{image_size}"
    ]

    category_args = []
    for cat in categories:
        category_args.extend(["-d", cat])

    args.extend(category_args)
    args.extend(["mvtec",
        "/work/mvtec_anomaly_detection",
    ])

    return args

def get_evaluate_args(results_dst_folder: str, model_paths: Sequence[str], categories: Tuple[str], resize: int = 256, image_size: int = 224) -> List[str]:
    args = [
        "command",
        "--seed",
        "0",
        results_dst_folder,
        "patch_core_loader"
    ]
    model_args = []
    for model_path in model_paths:
        model_args.extend(["--patch_core_paths", model_path])

    args.extend(model_args)

    args.extend([
        "dataset",
        "--resize",
        f"{resize}",
        "--imagesize",
        f"{image_size}",
    ])

    category_args = []
    for cat in categories:
        category_args.extend(["-d", cat])

    args.extend(category_args)
    args.extend(["mvtec", "/work/mvtec_anomaly_detection"])

    return args
