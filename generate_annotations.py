# -*- coding: utf-8 -*-
"""


@author: kishore saladi
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import patches

train = pd.read_csv('test.csv')
train.head()

image = plt.imread('test_images/apple_77.jpg')
plt.imshow(image)

train['filename'].nunique()

train['class'].value_counts()

fig = plt.figure()

#add axes to the image
ax = fig.add_axes([0,0,1,1])

# read and plot the image
image = plt.imread('test_images/apple_77.jpg')
plt.imshow(image)

# iterating over the image for different objects
for _,row in train[train.filename == "apple_77.jpg"].iterrows():
    xmin = row.xmin
    xmax = row.xmax
    ymin = row.ymin
    ymax = row.ymax
    
    width = xmax - xmin
    height = ymax - ymin
    
    rect = patches.Rectangle((xmin,ymin), width, height, edgecolor = 'r', facecolor = 'none')
    
    ax.add_patch(rect)
    
data = pd.DataFrame()
data['format'] = train['filename']

# as the images are in train_images folder, add train_images before the image name
for i in range(data.shape[0]):
    data['format'][i] = 'test_images/' + data['format'][i]
    
# add xmin, ymin, xmax, ymax and class as per the format required
for i in range(data.shape[0]):
    data['format'][i] = data['format'][i] + ',' + str(train['xmin'][i]) + ',' + str(train['ymin'][i]) + ',' + str(train['xmax'][i]) + ',' + str(train['ymax'][i]) + ',' + train['class'][i]

data.to_csv('annotate_text.txt', header=None, index=None, sep=' ')
