#!/usr/bin/env python
# Martin Kersner, m.kersner@gmail.com
# 2016/01/18 

import numpy as np

def pascal_classes():
  classes = {'beet_salad'       : 1,  'chicken_curry' : 2,  'chicken_wings': 3,  'chocolate_cake' : 4, 
             'frozen_yogurt'    : 5,  'fried_rice'    : 6,  'hamburger'    : 7,  'hot_dog'        : 8, 
             'hot_and_sour_soup': 9,  'ice_cream'     : 10, 'peking_duck'  : 11, 'pork_chop'      : 12, 
             'pho'              : 13, 'pizza'         : 14, 'ramen'        : 15, 'sushi'          : 16, 
             'club_sandwich'    : 17}


  return classes

def pascal_palette():
  palette = {(  0,   0,   0) : 0 , #000000
             ( 85,  85,  85) : 1 , #555555
             (102, 102, 102) : 2 , #666666
             (119, 119, 119) : 3 , #777777
             (136, 136, 136) : 4 , #888888
             (153, 153, 153) : 5 , #999999
             ( 51,  51,  51) : 6 , #333333 
             ( 17,  51,  68) : 7 , #113344
             ( 18,  52,  86) : 8 , #123456
             ( 17,  34,  51) : 9 , #112233
             (170, 170, 170) : 10, #AAAAAA
             (204, 204, 204) : 11, #CCCCCC
             (221, 221, 221) : 12, #DDDDDD
             ( 17,  17,  17) : 13, #111111
             ( 34,  34,  34) : 14, #222222 
             (238, 238, 238) : 15, #EEEEEE
             (187, 187, 187) : 16, #BBBBBB
             ( 68,  68,  68) : 17} #444444

  return palette

def palette_demo():
  palette_list = pascal_palette().keys()
  palette = ()
  
  for color in palette_list:
    palette += color

  return palette

def convert_from_color_segmentation(arr_3d):
  arr_2d = np.zeros((arr_3d.shape[0], arr_3d.shape[1]), dtype=np.uint8)
  palette = pascal_palette()

  # slow!
  for i in range(0, arr_3d.shape[0]):
    for j in range(0, arr_3d.shape[1]):
      key = (arr_3d[i,j,0], arr_3d[i,j,1], arr_3d[i,j,2])
      arr_2d[i, j] = palette.get(key, 0) # default value if key was not found is 0

  return arr_2d

def get_id_classes(classes):
  all_classes = pascal_classes()
  id_classes = [all_classes[c] for c in classes]
  return id_classes

def strstr(str1, str2):
  if str1.find(str2) != -1:
    return True
  else:
    return False

def create_lut(class_ids, max_id=256):
  # Index 0 is the first index used in caffe for denoting labels.
  # Therefore, index 0 is considered as default.
  lut = np.zeros(max_id, dtype=np.uint8)

  new_index = 1
  for i in class_ids:
    lut[i] = new_index
    new_index += 1

  return lut
