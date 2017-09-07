import os
import shutil 

f = open('train_list.txt', 'r')
f2 = open ('train.txt', 'w')
lines = f.readlines()
for line in lines:
  img_path = '/images/' + line[0:-1] + '.jpg'
  grd_path = '/ground_truths/' + line[0:-1] + '.png'
  line_to_write = img_path + ' ' + grd_path + '\n'
  f2.write(line_to_write )
f2.close()
f.close()
