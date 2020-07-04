# # convert picture to .png file

import os
from PIL import Image

def preprocessing(input_path,output_path):
    i=1
    for picture in os.listdir(input_path):
        im=Image.open(input_path+"/"+picture)
        im=im.convert("RGB")
        im.save(output_path+"/"+str(i)+".jpg")
        i+=1

preprocessing_1("/Users/manachu/Desktop/preprocessing_image_train_2","/Users/manachu/Desktop/train_2") #makeup_new train

preprocessing_1("/Users/manachu/Desktop/preprocessing_image_train_2","/Users/manachu/Desktop/train_2") #makeup_new test

# # Using opencv to capture person's face

import os
import cv2 as cv
from PIL import Image , ImageEnhance
import numpy as np
import sys 
import random
face_cascade = cv.CascadeClassifier('/anaconda3/lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_default.xml') #cv TODO 

def preprocessing_2(input_path,output_path):  
    i=1
    #k=[]
    for picture in os.listdir(input_path):
        #print(picture)
        im=Image.open(input_path+"/"+picture)
        im_wid ,im_hei= im.size
        box_a = (0, 0, im_wid/2, im_hei)
        box_b= (im_wid/2, 0, im_wid, im_hei)
        region_a = im.crop(box_a)
        region_b= im.crop(box_b)
        
      #A
    
        a_imgary = cv.cvtColor(np.asarray(region_a),cv.COLOR_RGB2BGR)  
        b_imgary=cv.cvtColor(np.asarray(region_b),cv.COLOR_RGB2BGR) 
        face_a= face_cascade.detectMultiScale(a_imgary)
        face_b= face_cascade.detectMultiScale(b_imgary)
        if (face_a ==() or face_b==()):
            continue
        else:
            k.append(int(picture[:-4]))
            x,y,w,h=face_a[0]
            new_a_img=region_a.crop((x,y,x+w,y+h)).resize((256,256))
            new_a_img.save(output_path + "/trainA/" + str(i) + "_a.jpg") #trainA need to revise to testA TODO
            Slice_a=random.sample([1,2,3,4,5,6],5)
            for photo_transform in Slice_a: #左右顛倒
                if photo_transform == 1:
                    new_a_img_1 = new_a_img.transpose(Image.FLIP_LEFT_RIGHT)
                    new_a_img_1.save(output_path + "/trainA/" + str(i) + "_trans_1_a.jpg") #trainA need to revise to testA TODO
                elif photo_transform ==2:  #旋轉15~45度在調整明亮度0.9~1.2
                    rand=random.randrange(15,46) 
                    brightness=random.uniform(0.9,1.2)
                    new_a_img_2 = new_a_img.rotate(rand)
                    new_a_img_2 = ImageEnhance.Brightness(new_a_img_2)
                    new_a_img_2 = new_a_img_2.enhance(brightness)
                    new_a_img_2.save(output_path + "/trainA/" + str(i) + "_trans_2_a.jpg") #trainA need to revise to testA TODO
                elif photo_transform ==3: #左右顛倒在旋轉 15~45度
                    rand=random.randrange(15,46) 
                    new_a_img_3 = new_a_img.transpose(Image.FLIP_LEFT_RIGHT)
                    new_a_img_3 = new_a_img_3.rotate(rand)
                    new_a_img_3.save(output_path + "/trainA/" + str(i) + "_trans_3_a.jpg") #trainA need to revise to testA TODO
                elif photo_transform ==4: #旋轉10~30度
                    rand=random.randrange(10,30)
                    new_a_img_4 = new_a_img.rotate(rand)
                    new_a_img_4.save(output_path + "/trainA/" + str(i) + "_trans_4_a.jpg")  #trainA need to revise to testA TODO

                elif photo_transform ==5:  #對比度調成0.7~1.5在調亮度0.9~1.2
                    new_a_img_5 = ImageEnhance.Contrast(new_a_img)
                    contrast = random.uniform(0.7,1.5)
                    new_a_img_5 = new_a_img_5.enhance(contrast)
                    new_a_img_5 = ImageEnhance.Brightness(new_a_img_5)
                    brightness=random.uniform(0.9,1.2)
                    new_a_img_5 = new_a_img_5.enhance(brightness)
                    new_a_img_5.save(output_path + "/trainA/" + str(i) + "_trans_5_a.jpg")  #trainA會需要改成testA
                elif photo_transform ==6: #調整銳度0.8~3.0在旋轉15~45度
                    new_a_img_6 = ImageEnhance.Sharpness(new_a_img)
                    sharpness = random.uniform(0.8,3.0)
                    new_a_img_6 = new_a_img_6.enhance(sharpness)
                    rand=random.randrange(15,46) 
                    new_a_img_6 = new_a_img_6.rotate(rand)
                    new_a_img_6.save(output_path + "/trainA/" + str(i) + "_trans_6_a.jpg")  #trainA need to revise to testA TODO
      #B  
        
            x_b,y_b,w_b,h_b=face_b[0]
            new_b_img=region_b.crop((x_b,y_b,x_b+w_b,y_b+h_b)).resize((256,256))
            new_b_img.save(output_path + "/trainB/" + str(i) + "_b.jpg") #trainB會需要改成testB
            Slice_b=random.sample([1,2,3,4,5,6],5)
            for photo_transform in Slice_b: #左右顛倒
                if photo_transform == 1:
                    new_b_img_1 = new_b_img.transpose(Image.FLIP_LEFT_RIGHT)
                    new_b_img_1.save(output_path + "/trainB/" + str(i) + "_trans_1_b.jpg") #trainB need to revise to testB TODO
                elif photo_transform ==2:  #旋轉15~45度在調整明亮度0.9~1.2
                    rand=random.randrange(15,46) 
                    brightness=random.uniform(0.9,1.2)
                    new_b_img_2 = new_b_img.rotate(rand)
                    new_b_img_2 = ImageEnhance.Brightness(new_b_img_2)
                    new_b_img_2 = new_b_img_2.enhance(brightness)
                    new_b_img_2.save(output_path + "/trainB/" + str(i) + "_trans_2_b.jpg") #trainB need to revise to testB TODO
                elif photo_transform ==3: #左右顛倒在旋轉 15~45度
                    rand=random.randrange(15,46) 
                    new_b_img_3 = new_b_img.transpose(Image.FLIP_LEFT_RIGHT)        
                    new_b_img_3 = new_b_img_3.rotate(rand)
                    new_b_img_3.save(output_path + "/trainB/" + str(i) + "_trans_3_b.jpg")  #trainB need to revise to testB TODO
                elif photo_transform ==4: #旋轉10~30度
                    rand=random.randrange(10,30)
                    new_b_img_4 = new_b_img.rotate(rand)
                    new_b_img_4.save(output_path + "/trainB/" + str(i) + "_trans_4_b.jpg")  #trainB會需要改成testB
                elif photo_transform ==5:  #對比度調成0.7~1.5在調亮度0.9~1.2
                    new_b_img_5 = ImageEnhance.Contrast(new_b_img)
                    contrast = random.uniform(0.7,1.5)
                    new_b_img_5 = new_b_img_5.enhance(contrast)
                    new_b_img_5 = ImageEnhance.Brightness(new_b_img_5)
                    brightness=random.uniform(0.9,1.2)
                    new_b_img_5 = new_b_img_5.enhance(brightness)
                    new_b_img_5.save(output_path + "/trainB/" + str(i) + "_trans_5_b.jpg") #trainB need to revise to testB TODO
                elif photo_transform ==6: #調整銳度0.8~3.0在旋轉15~45度
                    new_b_img_6 = ImageEnhance.Sharpness(new_b_img)
                    sharpness = random.uniform(0.8,3.0)
                    new_b_img_6 = new_b_img_6.enhance(sharpness)
                    rand=random.randrange(15,46) 
                    new_b_img_6 = new_b_img_6.rotate(rand)
                    new_b_img_6.save(output_path + "/trainB/" + str(i) + "_trans_6_b.jpg") #trainB need to revise to testB TODO
        i+=1


#run the function 
preprocessing_2("/Users/manachu/Desktop/train_1","/Users/manachu/Desktop/makeup_new") 


preprocessing_2("/Users/manachu/Desktop/test_1","/Users/manachu/Desktop/makeup_new") 


preprocessing_2("/Users/manachu/Desktop/train_2","/Users/manachu/Desktop/makeup_new_2") 

preprocessing_2("/Users/manachu/Desktop/test_2","/Users/manachu/Desktop/makeup_new_2") 
