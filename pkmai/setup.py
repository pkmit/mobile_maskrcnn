import os
import urllib.request as request
import zipfile
import sys

DATASET_URL = 'https://github.com/pkmit/mobile_maskrcnn/releases/download/1.0/dataset.zip'
WEIGHT_URL = 'https://github.com/pkmit/mobile_maskrcnn/releases/download/1.0/mobile_mask_rcnn_coco.h5'

ROOT_DIR = os.path.join(os.getcwd(), 'pkmai')
DATASET_DIR = os.path.join(ROOT_DIR, 'dataset')
DATASET_FILE_PATH = os.path.join(DATASET_DIR, 'dataset.zip')
WEIGHT_DIR = os.path.join(ROOT_DIR, 'weights')

def report_progress(count, blockSize, totalSize):
  	percent = int(count*blockSize*100/totalSize)
  	sys.stdout.write("\r%d%%" % percent + ' complete')
  	sys.stdout.flush()

if not os.path.isdir(DATASET_DIR):
    print('Setting up dataset folder')
    os.mkdir(DATASET_DIR)

print('Downloading and extracting dataset')
request.urlretrieve(DATASET_URL, DATASET_FILE_PATH, reporthook=report_progress)
with zipfile.ZipFile(DATASET_FILE_PATH, 'r') as z:
    z.extractall(DATASET_DIR)

if not os.path.isdir(WEIGHT_DIR):
    print('Create weight folder')
    os.makedirs(WEIGHT_DIR)

print('Downloading weight')
request.urlretrieve(WEIGHT_URL, os.path.join(WEIGHT_DIR, 'base.h5'), reporthook=report_progress)

print('Done')