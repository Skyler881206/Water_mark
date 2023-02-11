import os
import cv2
import numpy as np

if __name__ == "__main__":
    BIT_VALUE = 3
    IMAGE_SIZE = (512, 512)
    IMAGE_0_PATH = r"C:\Users\Skyler\Desktop\Course\Image_Processing\LAB1\0.jpg"
    IMAGE_1_PATH = r"C:\Users\Skyler\Desktop\Course\Image_Processing\LAB1\1.jpg"
    SAVE_PATH = r"C:\Users\Skyler\Desktop\Course\Image_Processing\LAB1\result"

    Image_0 = cv2.resize(cv2.imread(IMAGE_0_PATH, 0), IMAGE_SIZE) # Read Image for gray scale mode and resize to same size
    Image_1 = cv2.resize(cv2.imread(IMAGE_1_PATH, 0), IMAGE_SIZE)

    Image_0 = Image_0.reshape(-1, 1) # Reshape image to (w*h, 1)
    Image_1 = Image_1.reshape(-1, 1)

    Image_0 = np.unpackbits(Image_0, axis=1) # Unpack to 8bit
    Image_1 = np.unpackbits(Image_1, axis=1)

    # -------------------
    for i in range(BIT_VALUE): # 1, 2, 3 bit
        Image_Watermark = np.zeros(Image_0.shape, dtype=np.uint8) # Get watermark image size and assign it to zero value
        Image_Watermark_Lite = np.zeros(Image_0.shape, dtype=np.uint8) # Get watermark and assign it to zero
        for j in range(Image_0.shape[0]):
            Image_Watermark_Lite[j][:i+1] = Image_1[j][7-i:] # Enhance watermark from LSB to MSB. It can more easy to visualization the result
            Image_Watermark[j][:7-i] = Image_0[j][:7-i] # Get Origianl image bit
            Image_Watermark[j][7-i] = Image_1[j][7-i] # Cover watermark
        
        IMAGE_SAVE_PATH = os.path.join(SAVE_PATH, str(i + 1) + "_bit")

        Watermark = np.packbits(Image_Watermark, axis=1)
        Watermark_Lite = np.packbits(Image_Watermark_Lite, axis=1)
        Watermark = Watermark.reshape(IMAGE_SIZE) # Reshape to IMAGE_SIZE
        Watermark_Lite = Watermark_Lite.reshape(IMAGE_SIZE)
        cv2.imwrite(IMAGE_SAVE_PATH + "_WATERMARK.jpg", Watermark) # Save image
        cv2.imwrite(IMAGE_SAVE_PATH + "_WATERMARK_LITE.jpg", Watermark_Lite)