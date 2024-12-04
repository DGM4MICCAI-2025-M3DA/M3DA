# Calgary-Campinas Public Dataset (CC359) 

Learn the details about this dataset in the
[paper](https://www.sciencedirect.com/science/article/abs/pii/S105381191730668).
The CC359 dataset is available under CC BY-ND 4.0 licence.

## Description

This paper presents an open, multi-vendor, multi-field strength magnetic resonance (MR)
T1-weighted volumetric brain imaging dataset, named Calgary-Campinas-359 (CC359). 

The dataset is composed of images of older healthy adults (29–80 years)
acquired on scanners from three vendors (Siemens, Philips and General Electric) at both 1.5 T and 3 T.
CC359 is comprised of 359 datasets, approximately 60 subjects per vendor and magnetic field strength. 

The dataset is approximately age and gender balanced, subject to the constraints of the available images.
It provides consensus brain extraction masks for all volumes generated using supervised classification

For more details, visit the [official homepage](https://sites.google.com/view/calgary-campinas-dataset/home)
or the [legacy homepage](https://miclab.fee.unicamp.br/calgary-campinas-359-updated-05092017).

## Download

To obtain MR images and brain and hippocampus segmentation masks,
please follow the instructions at the download [platform](https://portal.conp.ca/dataset?id=projects/calgary-campinas).

### Using `datalad` library
You need to download three zip archives:
- `Original.zip` (the original MR images)
- `hippocampus_staple.zip` (Silver-standard hippocampus masks generated using STAPLE)
- `Silver-standard-machine-learning.zip` (Silver-standard brain masks generated using a machine learning method)

### Downloading WM, GM, and CSF Masks
To the current date, WM, GM, and CSF masks can only be downloaded from the
[Google Drive folder](https://drive.google.com/drive/u/0/folders/0BxLb0NB2MjVZNm9JY1pWNFp6WTA?resourcekey=0-2sXMr8q-n2Nn6iY3PbBAdA).

Here, you need to manually download the folder `CC359/Reconstructed/CC359/WM-GM-CSF/`.

### Folder Structure
So the root folder to pass to the dataset class should contain four objects:
- Three zip archives:
  - `<...>/Original.zip`
  - `<...>/hippocampus_staple.zip`
  - `<...>/Silver-standard-machine-learning.zip`
- One folder:
  - `WM-GM-CSF` with the original structure:
    ```
    <...>/WM-GM-CSF/CC0319_ge_3_45_M.nii.gz
    <...>/WM-GM-CSF/CC0324_ge_3_56_M.nii.gz
    ```
    
`<...>` means the root folder, e.g., `/path/to/the/downloaded/files/cc359/`.

## Usage
You can process the CC359 dataset using the
[`amid`](https://github.com/neuro-ml/amid/tree/master) library. Below is an example of how to use it:

```python
from amid.cc359 import CC359 

cc359 = CC359(root='/path/to/the/downloaded/files/cc359/')
len(cc359.ids)  # 359
cc359.image(cc359.ids[0]).shape  # (171, 256, 256)
cc359.wm_gm_csf(cc359.ids[80]).shape  # (180, 240, 240)
```

## Citation
If you found this dataset useful for your research, please cite:

```bibtex
@article{SOUZA2018482,
title = {An open, multi-vendor, multi-field-strength brain MR dataset and analysis of publicly available skull stripping methods agreement},
journal = {NeuroImage},
volume = {170},
pages = {482-494},
year = {2018},
note = {Segmenting the Brain},
issn = {1053-8119},
doi = {https://doi.org/10.1016/j.neuroimage.2017.08.021},
url = {https://www.sciencedirect.com/science/article/pii/S1053811917306687},
author = {Roberto Souza and Oeslle Lucena and Julia Garrafa and David Gobbi and Marina Saluzzi and Simone Appenzeller and Letícia Rittner and Richard Frayne and Roberto Lotufo},
keywords = {Public database, Skull stripping, Brain extraction, Brain segmentation, Brain MR image analysis, MP-RAGE},
abstract = {This paper presents an open, multi-vendor, multi-field strength magnetic resonance (MR) T1-weighted volumetric brain imaging dataset, named Calgary-Campinas-359 (CC-359). The dataset is composed of images of older healthy adults (29–80 years) acquired on scanners from three vendors (Siemens, Philips and General Electric) at both 1.5 T and 3 T. CC-359 is comprised of 359 datasets, approximately 60 subjects per vendor and magnetic field strength. The dataset is approximately age and gender balanced, subject to the constraints of the available images. It provides consensus brain extraction masks for all volumes generated using supervised classification. Manual segmentation results for twelve randomly selected subjects performed by an expert are also provided. The CC-359 dataset allows investigation of 1) the influences of both vendor and magnetic field strength on quantitative analysis of brain MR; 2) parameter optimization for automatic segmentation methods; and potentially 3) machine learning classifiers with big data, specifically those based on deep learning methods, as these approaches require a large amount of data. To illustrate the utility of this dataset, we compared to the results of a supervised classifier, the results of eight publicly available skull stripping methods and one publicly available consensus algorithm. A linear mixed effects model analysis indicated that vendor (p−value<0.001) and magnetic field strength (p−value<0.001) have statistically significant impacts on skull stripping results.}
}