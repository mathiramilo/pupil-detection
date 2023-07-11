from argparse import ArgumentParser
from src import segment

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--img_path', type=str, default='dataset/10/1/1_001.jpg')
    args = parser.parse_args()

    segment.segmentate(args.img_path)
    
    