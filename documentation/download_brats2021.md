# BraTS2021
The BraTS 2021 data of 2,000 cases (8,000 mpMRI scans).
All BraTS mpMRI scans are available as NIfTI files (.nii.gz) for segmentation
and as DICOM (.dcm) files for classification.
The dataset is available under CC BY 4.0 licence.

## Description
BraTS2021 includes:
- Multi-modal MRI scans from patients with brain tumors, including T1, T1Gd, T2, and FLAIR sequences.
- Segmentation masks annotated with tumor sub-regions: 
  - GD-enhancing tumor (ET — label 4)
  - Peritumoral edematous/invaded tissue (ED — label 2)
  - Necrotic tumor core (NCR — label 1)

The ground truth data were created after pre-processing:
co-registered to the same anatomical template, interpolated to the same resolution (1 mm^3) and skull-stripped.

For more details, visit the [official website](http://www.braintumorsegmentation.org/).

## Download
The dataset can be downloaded from the following link:
[Download BraTS2021](http://www.braintumorsegmentation.org/)

After downloading, place the dataset archives in a directory of your choice, e.g.,
`/path/to/the/downloaded/files/brats2021/`.

## Usage
You can process the BraTS2021 dataset using the [`amid`](https://github.com/neuro-ml/amid/tree/master) library.
Below is an example of how to use it:

```python
from amid.brats2021 import BraTS2021

ds = BraTS2021(root='/path/to/the/downloaded/files/brats2021/')
len(ds.ids)  # 5880
ds.image(ds.ids[0]).shape  # (240, 240, 155)
```

## Citation
If you use the BraTS2021 dataset in your research, please cite the following paper
(and others, as listed on the official website):

```bibtex
@article{brats2021,
  author = {Menze, Bjoern H. and Jakab, Andras and Bauer, Stefan and Kalpathy-Cramer, Jayashree and Farahani, Keyvan and Kirby, Justin and Burren, Yves and Porz, Nicole and Slotboom, Johannes and Wiest, Roland and others},
  title = {The BraTS 2021 Benchmark on Brain Tumor Segmentation},
  journal = {International MICCAI BraTS Challenge},
  year = {2021},
  url = {http://www.braintumorsegmentation.org/}
}
