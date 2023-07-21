import glob
import os
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from typing import Callable

import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import FuncFormatter

from dummy import dummy_method
from segment import find_pupil

# def plot_cumulative_error(algorithm_errors : list[np.ndarray],
#                           titles : list[str],
#                           plot_name : str = "cumulative_error.png"
#                           ) -> None:
#     total_samples = len(algorithm_errors[0])
#     errors = []
#     for err in algorithm_errors:
#         errors.extend(err)
#     x_values = sorted(set(errors))
    
#     fig, ax = plt.subplots()
   
#     # Plot cumulative error distribution
#     for errors, title in zip(algorithm_errors, titles):
#         alg_err_dist = [sum(1 for error in errors if error <= x) / total_samples for x in x_values]
#         ax.plot(x_values, alg_err_dist, label=title)
        
#     ax.set_ylabel("Percentage of Images")
#     ax.set_xlabel("Detection Error")
#     ax.set_title("Cumulative Error Distribution of Each Algorithm")

#     # Set tick labels with units using formatters
#     ax.xaxis.set_major_formatter(FuncFormatter(lambda x, pos: f"{x:.0f}px"))
#     ax.yaxis.set_major_formatter(FuncFormatter(lambda y, pos: f"{y*100:.0f}%"))

#     ax.legend()
#     plt.savefig(plot_name)


# def test(image_path: str):
#     pass
    

# def euclidean_dist(x : float, y : float) -> float:
#     return np.sqrt(np.sum((x - y)**2))

# def test_all_images(method : Callable[[np.ndarray]], dataset_path : str, error_fn: Callable[[float, float], float] = euclidean_dist) -> None:
#     # 132000 frames en total = 22(subcarpetas) * 3(videos_en_subcarpeta) * 2000(frames_por_video)
    
#     for subfolder_idx in range(1, 23):
#         subfolder = f"{dataset_path}/{subfolder_idx}/"
        
#         annot_path = f"{subfolder}/{subfolder_idx}.txt"

#         ground_truth = pd.read_csv(annot_path, sep=" ", header=None)
#         ground_truth.columns = ["x", "y"]

#         results = []
#         for frame in range(1, 2001):
#             img = cv2.imread(f"{subfolder}/{subfolder_idx}_frames/frame_{frame}.png")
#             error = error_fn(ground_truth.iloc[frame-1].values, method(img))
#             results.append(error)
        
#         rand_errs = np.random.randint(0, 300, size=len(results))
#         rand_errs2 = np.random.randint(0, 300, size=len(results))
#         plot_cumulative_error([results, rand_errs, rand_errs2], 
#                             ["Dummy", "Random1", "Random2"])
        

def error_fn(x : float, y : float) -> float:
    return np.sqrt(np.sum((x - y)**2))

def process_subfolder(subfolder_idx):
    subfolder = f"{dataset_path}/{subfolder_idx}/"
    
    for annot_path in Path(subfolder).glob("*.txt"):
        ground_truth = pd.read_csv(annot_path, sep=" ", header=None)
        ground_truth.columns = ["x", "y"]

        video_number = annot_path.stem
        for frame in range(1, 2001):
            img = cv2.imread(f"{subfolder}/{video_number}_frames/frame_{frame}.png")
            pupil = find_pupil(img)
            if pupil is None:
                continue
            x, y = ground_truth.iloc[frame-1].values
            _, (c_x, c_y) = pupil
            error = error_fn(c_x - x, c_y - y)
            results.append(error)
            
if __name__ == "__main__":
    DATASET_DIR = "../dataset/LPW_frames/LPW/" # TODO : desharcodear
    dataset_path = DATASET_DIR
    MAX_FOLDER = 23  # <23

    results = []

    with ProcessPoolExecutor() as executor:
        for subfolder_idx in range(1, MAX_FOLDER):
            future = executor.submit(process_subfolder, subfolder_idx)
            results.append(future)

    # Gather results from all the processes
    final_results = []
    for future in results:
        final_results.extend(future.result())