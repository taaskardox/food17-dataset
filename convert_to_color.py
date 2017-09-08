from __future__ import print_function
import os
import sys
from skimage.io import imread, imsave
import numpy as np
import json
from PIL import PngImagePlugin, Image
import caffe

def main():
  ##
  ext = '.png'
  ##

  path, txt_file, out_path = process_arguments(sys.argv)
  with open('pascal_voc.json', 'r') as fp:
    info = json.load(fp)
  palette = np.array(info['palette'], dtype=np.uint8)

  with open(txt_file, 'rb') as f:
    for img_name in f:
      img_base_name = img_name.strip()
      img_name = os.path.join(path, img_base_name) + ext
      img = imread(img_name)
      out_path = 'color_grd/'+ img_base_name + '.png'
      
      im = Image.fromarray(img, mode='P')
      im.putpalette(palette.flatten())
      im.save(out_path)

def process_arguments(argv):
  if len(argv) != 4:
    help()

  path = argv[1]
  list_file = argv[2]
  out_path = argv[3]


  return path, list_file, out_path

def help():
  print('Wrong arguments'
        , file=sys.stderr)
  
  exit()

if __name__ == '__main__':
  main()
