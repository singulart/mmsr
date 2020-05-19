import cv2
import glob
import os
import tqdm
from itertools import islice
from multiprocessing import Pool
from pathlib import Path

path = r'F:\!Lapenko\60FPS-bicubic\*.png'
split_img_amount = (5, 5)  # Height, Width
split_dir = [['_{}_{}'.format(i, j) for j in range(split_img_amount[1])] for i in range(split_img_amount[0])]


def split_image(_file):
    img = cv2.imread(_file, cv2.IMREAD_UNCHANGED)
    if img.shape[0] % split_img_amount[0] != 0 or img.shape[1] % split_img_amount[1] != 0:
        raise ValueError('Image resolution is not the multiple of number of split image')
    stride = (img.shape[0] // split_img_amount[0], img.shape[1] // split_img_amount[1])
    for i in range(split_img_amount[0]):
        for j in range(split_img_amount[1]):
            split_img = img[i * stride[0]:(i + 1) * stride[0], j * stride[1]:(j + 1) * stride[1], :]
            dirname = os.path.dirname(_file)
            save_path = os.path.join(os.path.dirname(dirname), os.path.basename(dirname) + split_dir[i][j],
                                     os.path.basename(_file))
            Path(os.path.dirname(save_path)).mkdir(parents=True, exist_ok=True)
            cv2.imwrite(save_path, split_img)


if __name__ == '__main__':
    num_process = 16
    files = glob.glob(path, recursive=True)
    # iter_files = iter(files)
    # files = [list(islice(iter_files, e)) for e in [len(files) // num_process] * (num_process + 1)]
    with Pool(processes=num_process) as p:
        r = list(tqdm.tqdm(p.imap(split_image, files), total=len(files)))
