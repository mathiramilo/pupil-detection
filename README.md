![logo-fing-udelar](https://github.com/mathiramilo/Pupil-Detection/assets/42822912/64d79044-a2d4-4ba5-bde0-44d66a8b0eb3)
# Computer Image Processing Final Project - Pupil Detection

Pupil detection in human eye images using image processing techniques with python.

## Website

Learn more about this project by visiting it's website in the following URL:

https://mathiasramilo.pages.fing.edu.uy/proyecto-final-timag/

## Usage

On Linux:

- Install the required packages:

```bash
pip3 install -r requirements.txt
```

- Segment pupil on a single image:

```bash
python cli_runner.py --image_path <path_to_image>
```

> Note: omitting the `--image_path` argument will run the program on a default image.

- Evaluate the model over a folder of images:

```bash
python cli_runner.py --folder_path <path_to_folder>
```

> Note: omitting the `--folder_path` argument will run the program on a default folder.

- Evaluate the model over a dataset:

```bash
python cli_runner.py --dataset_path <path_to_dataset>
```

> Note: omitting the `--dataset_path` argument will run the program on a default dataset. Moreover it will run over the LPW dataset.

## Dataset

- [Dataset Website](https://www.mpi-inf.mpg.de/departments/computer-vision-and-machine-learning/research/gaze-based-human-computer-interaction/labelled-pupils-in-the-wild-lpw)
- [Paper Link](https://arxiv.org/pdf/1511.05768.pdf)

# Review of State of the Art Eye Gaze Estimation Methods

D. W. Hansen and Q. Ji, "In the Eye of the Beholder: A Survey of Models for Eyes and Gaze," in IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 32, no. 3, pp. 478-500, March 2010, doi: 10.1109/TPAMI.2009.30.

### Primary Source

This paper served as our primary source, aiming not only to reference its findings but also to faithfully reproduce the results it achieved.

- [Citation](https://www.hci.uni-tuebingen.de/assets/pdf/publications/WTCKWE092015.pdf)
