#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import os 
import shutil


# In[6]:


#create datasets for positive samples 
FILE_PATH=r"C:\Users\HARSHIT SINGHAL\Desktop\covid detection data set\covid-chestxray-dataset\metadata.csv"

IMAGE_PATH=r"C:\Users\HARSHIT SINGHAL\Desktop\covid detection data set\covid-chestxray-dataset\images"


# In[7]:


df=pd.read_csv(FILE_PATH)


# In[7]:


df


# In[8]:


df.shape


# In[24]:


TARGET_DIR="C:/Users/HARSHIT SINGHAL/Desktop/covid detection data set/Dataset/Covid"


if not os.path.exists(TARGET_DIR) :
    os.mkdir(TARGET_DIR)
    print("Covid folder Created")
    


# In[35]:


cnt=0
for (i,row) in df.iterrows():
    if row["finding"]=="Pneumonia/Viral/COVID-19"and row["view"]=="PA":
        
        filename=row["filename"]
        image_path=os.path.join(IMAGE_PATH,filename)
        image_copy_path=os.path.join(TARGET_DIR,filename)
        shutil.copy2(image_path,image_copy_path)
        #print("Moving  Images",cnt)
        cnt+=1
    



print(cnt)


# In[10]:


#sampling of datasets  from kaggle datasets

import random
KAGGLE_FILE_PATH="C:/Users/HARSHIT SINGHAL/Desktop/covid detection data set/chest_xray/train/NORMAL"
TARGET_NORMAL_DIR="C:/Users/HARSHIT SINGHAL/Desktop/covid detection data set/Dataset/Normal"


# In[39]:


random.seed(5)


# In[11]:


image_names=os.listdir(KAGGLE_FILE_PATH)


# In[12]:


image_names


# In[ ]:


random.shuffle(image_names)


# In[13]:


for i in range(196):
    image_name=image_names[i]
    image_path=os.path.join(KAGGLE_FILE_PATH,image_name)
    
    target_path=os.path.join(TARGET_NORMAL_DIR,image_name)
    shutil.copy2(image_path,target_path)
    print("Copying image",i)
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




