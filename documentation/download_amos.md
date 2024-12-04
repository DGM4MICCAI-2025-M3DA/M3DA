 # AMOS

AMOS is a large-scale dataset for medical image segmentation,
designed as a benchmark for studying robust segmentation algorithms in diverse scenarios.
It is available under CC BY 4.0 licence.

## Description
 AMOS includes:
- **500** CT scans and **100** MRI scans.
- Voxel-level annotations for **15 abdominal organs**.
- Diverse data: multi-center, multi-vendor, multi-modality, multi-phase,    multi-disease patients.

This dataset provides challenging examples suitable for testing and training state-of-the-art segmentation methods.

For more details about AMOS, refer to the paper
[**AMOS: A Large-Scale Abdominal Multi-Organ Benchmark for Versatile Medical Image Segmentation**](https://arxiv.org/abs/2206.08023)  


## Download

The dataset can be downloaded from the following link [download AMOS](https://zenodo.org/records/7262581), file `amos22.zip`

After downloading, make sure the data is placed in an appropriate directory, e.g.,
`/path/to/the/downloaded/files/amos22/`.

## Usage
You can process the AMOS dataset using the [`amid`](https://github.com/neuro-ml/amid/tree/master) library. Below is an example of how to use it:


```
from amid.amos import AMOS

ds = AMOS(root='/path/to/the/downloaded/files/amos22/')
len(ds.ids)  # 961
ds.image(ds.ids[0]).shape  # (768, 768, 90)
ds.mask(ds.ids[26]).shape  # (512, 512, 124)
```

## Useful Links

- Documentation for the [AMOS class](https://github.com/neuro-ml/amid/blob/master/amid/amos/dataset.py):
explains the available functionalities.

- [AMID](https://github.com/neuro-ml/amid/tree/master) repository: for additional examples and support.

## Citation

If you found this dataset useful for your research, please cite:

```bibtex
@inproceedings{NEURIPS2022_ee604e1b,
 author = {Ji, Yuanfeng and Bai, Haotian and GE, Chongjian and Yang, Jie and Zhu, Ye and Zhang, Ruimao and Li, Zhen and Zhanng, Lingyan and Ma, Wanling and Wan, Xiang and Luo, Ping},
 booktitle = {Advances in Neural Information Processing Systems},
 editor = {S. Koyejo and S. Mohamed and A. Agarwal and D. Belgrave and K. Cho and A. Oh},
 pages = {36722--36732},
 publisher = {Curran Associates, Inc.},
 title = {AMOS: A Large-Scale Abdominal Multi-Organ Benchmark for Versatile Medical Image Segmentation},
 url = {https://proceedings.neurips.cc/paper_files/paper/2022/file/ee604e1bedbd069d9fc9328b7b9584be-Paper-Datasets_and_Benchmarks.pdf},
 volume = {35},
 year = {2022}
}
