from __future__ import print_function
import os
import sys
from skimage.io import imread, imsave

def main():
  ##
  ext = '.jpg'
  ##

  path, txt_file = process_arguments(sys.argv)


  with open(txt_file, 'rb') as f:
    for img_name in f:
      img_base_name = img_name.strip()
      img_name = os.path.join(path, img_base_name) + ext
      img = imread(img_name)

      if (len(img.shape) > 2):
	print(img)
      else:
        print(img_name + " is not composed of three dimensions, therefore " 
              "shouldn't be processed by this script.\n"
              "Exiting." , file=sys.stderr)

        exit()

def process_arguments(argv):
  if len(argv) != 3:
    help()

  path = argv[1]
  list_file = argv[2]


  return path, list_file

def help():
  print('Wrong arguments'
        , file=sys.stderr)
  
  exit()

if __name__ == '__main__':
  main()
