import os

local = True
jarvis = False

# for train
if local:
    base_dir = './detection_test/'
    img_dir = base_dir
    train_txt_file = './testlabel.txt'

else:
    base_dir = '/data/yintianshu/data/images/'
    img_dir = base_dir
    train_txt_file = './label.txt'


# for test

if local:
    model_path = "./checkpoints/ctpn_ep49_0.0274_0.0262_0.0300.pth.tar"
    img_path = './detection_test/'

else:
    model_path = "./checkpoints/ctpn_ep49_0.2636_0.0039_0.2674.pth.tar"
    img_path = './detection_test/'

anchor_scale = 16
IOU_NEGATIVE = 0.3
IOU_POSITIVE = 0.7
IOU_SELECT = 0.7

RPN_POSITIVE_NUM = 15
RPN_TOTAL_NUM = 45

# bgr can find from  here: https://github.com/fchollet/deep-learning-models/blob/master/imagenet_utils.py
IMAGE_MEAN = [123.68, 116.779, 103.939]


checkpoints_dir = './checkpoints'
outputs = './logs'
