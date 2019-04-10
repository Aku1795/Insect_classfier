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

We trained a SVM model on the HOG of the pictures to predict either it's an insect or not. Then for locating the insect in the picture we use a sliding window and keep the parts very likely to englobe an insect with a heatmap.

Please find in the ./Preprocessing/HOG_SVM folder the jupyter notebooks explaining the different tasks:
- feature_sourcer_test.ipynb: test the HOG feature sourcer
- classifier_training.ipynb: train the SVM
- HOG_SVM_grid_search.ipynb: find best params for model
- slider_test.ipynb: show sliding window
- heatmap_test.ipynb: show the heatmap functionality

## Image Classification

Two approaches were explored to classify insect pictures. On one hand a CNN was trained from scratch using the Keras modules and Google Colab computing resources. On the other hand a Fine Tuning approached was implemented using the pre-trained Resnet network and Pytorch modules.


### CNN from scratch


### Transfer learning and fine tuning

