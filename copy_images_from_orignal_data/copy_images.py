import os
import shutil 

classes = ['fried_rice', 'club_sandwich', 'beet_salad', 'chicken_curry', 'chicken_wings', 'chocolate_cake', 'frozen_yogurt', 'ice_cream', 'sushi', 'peking_duck', 'pork_chop', 'ramen', 'hot_dog', 'hot_and_sour_soup', 'hamburger', 'pho', 'pizza']
img_root = '/home/khanhngan/tuan.khai/DeepLab-Context/food_data/images/'


for cl in classes:
  file_name = cl + '.txt'
  f = open(file_name, 'r')
  img_folder = img_root + cl + '/';
  if not os.path.exists(img_folder):
    os.makedirs(img_folder)
  lines = f.readlines()
  for line in lines:
    img_file_name = line[0:-1] +'.jpg'
    img_file = '../' + cl+ '/' + img_file_name
    shutil.copy2(img_file, img_root + img_file_name, )
  f.close()
  
