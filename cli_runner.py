from argparse import ArgumentParser
from src import segment
from src import test

DATASET_DIR = "dataset/LPW_frames/LPW"
PLOTS_DIR = "plots"

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--img_path', type=str, default=f'{DATASET_DIR}/1/1_frames/frame_1.png')
    parser.add_argument('--dataset_path', type=str, default=DATASET_DIR)
    args = parser.parse_args()
    
    if args.img_path is not None:
        # guardar la imagen con la pupila detectada marcada
        segment.process_image(PLOTS_DIR, args.img_path)
    elif args.dataset_path is not None:
        # guardar cumulative plot en la carpeta plot 
        test.test_dataset(args.dataset_path)

    
    