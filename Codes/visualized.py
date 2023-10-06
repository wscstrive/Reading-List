# -*- coding: utf-8 -*-
# @Description: visualized
# @Author: elleryw, NUIST
# @Date: 2023-10-06 22:37:06
# @LastEditTime:


import numpy as np
import re
import sys, os
import matplotlib.pyplot as plt
from PIL import Image
import cv2

def visual_depth(depth, color_reverse=False):
    plt.figure(figsize=(12, 12))
    plt.subplot(1, 2, 1)
    plt.xticks([]), plt.yticks([]), plt.axis('off')
    if color_reverse:
        plt.imshow(depth, 'viridis_r', vmin=500, vmax=830)
    else:
        plt.imshow(depth, 'viridis')
