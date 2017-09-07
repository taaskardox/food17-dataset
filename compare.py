from __future__ import print_function
import os
import sys
from skimage.io import imread, imsave

def main():
  ##
  ext1 = '.jpg'
  ext2 = '.png'
  ##

  path1, path2, txt_file = process_arguments(sys.argv)


  with open(txt_file, 'rb') as f:
    for img_name in f:
      img_base_name = img_name.strip()
      img_name1 = os.path.join(path1, img_base_name) + ext1
      img1 = imread(img_name1)

      img_name2 = os.path.join(path2, img_base_name) + ext2
      img2 = imread(img_name2)

      if (img1.shape[0] !=  img2.shape[0] or img1.shape[1] != img2.shape[1]):
	print(img_base_name)
        exit()

def process_arguments(argv):
  if len(argv) != 4:
    help()

  path1 = argv[1]
  path2 = argv[2]
  list_file = argv[3]


  return path1, path2, list_file

def help():
  print('Usage: python convert_labels.py PATH LIST_FILE NEW_PATH\n'
        'PATH points to directory with segmentation image labels.\n'
        'LIST_FILE denotes text file containing names of images in PATH.\n'
        'Names do not include extension of images.\n'
        'NEW_PATH points to directory where converted labels will be stored.'
        , file=sys.stderr)
  
  exit()

if __name__ == '__main__':
  main()
