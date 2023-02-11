# LAB_1 WATER MARK

[TOC]

## Introduction

In this work, we make a watermark generator for 2 images can conbine bitwise.

## Coding Detail

### Environment
We use Python environment by version **3.8**, and use cv2, numpy to calculate the watermark image.

### Constant
Input Image: ./0.jpg, ./1.jpg
Output Image: ./result/1_bit_WATERMARK.jpg, 1_bit_WATERMARK_LITE.jpg...

IMAGE_SIZE: Resize image size to specific size
BIT_VALUE: How many bits want to be watermark background

IMAGE_0_PATH: Original Image PATH
IMAGE_1_PATH: Watermark Image PATH
SAVE_PATH: Saving Image PATH

### Design Detail

We use cv2 package to read Image, and resize it. Futher we reshape image to (W x H, 1) size and unpack it to (W x h, 8).

Then bit-wise replace the image and pack it to uint8 format and reshape to previous IMAGE_SIZE. 
Final we using cv.imwrite to save watermark image.