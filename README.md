# Proyecto Final TIMAG

## Table of Contents

## Introduction

## Requirements
## Usage
On Linux:
* Install the required packages:
```bash
pip3 install -r requirements.txt
```
* Segment pupil on a single image:
```bash
python cli_runner.py --image_path <path_to_image>
```
> Note: omitting the `--image_path` argument will run the program on a default image.
* Evaluate the model over a dataset:
```bash
python cli_runner.py --dataset_path <path_to_dataset>
```
> Note: omitting the `--dataset_path` argument will run the program on a default dataset. Moreover it will run over the LPW dataset.



## Dataset 
D. W. Hansen and Q. Ji, "In the Eye of the Beholder: A Survey of Models for Eyes and Gaze," in IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 32, no. 3, pp. 478-500, March 2010, doi: 10.1109/TPAMI.2009.30.
- [Dataset Website](https://www.mpi-inf.mpg.de/departments/computer-vision-and-machine-learning/research/gaze-based-human-computer-interaction/labelled-pupils-in-the-wild-lpw)
- [Paper Link](https://arxiv.org/pdf/1511.05768.pdf)

## Results

## References
### Primary Source
This paper served as our primary source, aiming not only to reference its findings but also to faithfully reproduce the results it achieved.
- [Citation]()
