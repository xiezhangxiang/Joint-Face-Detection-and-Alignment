#!/usr/bin/env python2.7
# coding = utf-8

import os


# dataDir contains `WIDER`, `CelebA`, `aflw`
data_dir = os.path.dirname(os.path.abspath(__file__))
# dataWIDER contains `WIDER_train`, `WIDER_val`, `WIDER_test`, `wider_face_split`
data_wider = os.path.join(data_dir, 'WIDER')
# dataCelebA contains `img_celeba`, `list_landmarks_celeba.txt`
data_celeba = os.path.join(data_dir, 'CelebA')

config = {
  'data_dir': data_dir,
  'data_wider': data_wider,
  'data_celeba': data_celeba
}

if __name__ == '__main__':
  print config
