# Insect_classifier
## Computer Vision, Datamining and Deep Learning  project, CentraleSupélec 2019

- *Aubin Victor*
- *Grandjouan Paul*
- *Than Marc*

Data Science project for the class of Deep Learning, Computer Vision and Datamining at CentraleSupelec using computer vision and deep learning techniques to classify insects - namingly flies, mosquitoes, butterflies and bees.

## Datasets

We found insects pictures from gbif.org by scrapping images. We have a total of 2000 pictures by species. You can find a sample dataset with 200 pictures by species in ./ExampleDataset

## Preprocessing

The preprocessing step aims to locate the mosquito in the picture in order to crop it and make better predictions after.

We trained an SVM 

Please find in the ./Preprocessing folder the jupyter notebooks showing the method.

## Image Classification

Two approaches were explored to classify insect pictures. On one hand a CNN was trained from scratch using the Keras modules and Google Colab computing resources. On the other hand a Fine Tuning approached was implemented using the pre-trained Resnet network and Pytorch modules.


### CNN from scratch


### Transfer learning and fine tuning

