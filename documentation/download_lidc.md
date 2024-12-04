# LIDC

The (L)ung (I)mage (D)atabase (C)onsortium image collection (LIDC-IDRI)
consists of diagnostic and lung cancer screening thoracic computed tomography (CT) scans
with marked-up annotated lesions and lung nodules segmentation task. Scans contains multiple expert annotations.
The dataset is available under CC BY 3.0 licence.

## Description

Seven academic centers and eight medical imaging companies collaborated to create this data set
which contains 1018 cases. Each subject includes images from a clinical thoracic CT scan
and an associated XML file that records the results of a two-phase image annotation process
performed by four experienced thoracic radiologists. In the initial blinded-read phase,
each radiologist independently reviewed each CT scan and marked lesions belonging to one of three categories
("nodule > or =3 mm," "nodule <3 mm," and "non-nodule > or =3 mm"). In the subsequent unblinded-read phase,
each radiologist independently reviewed their own marks along with the anonymized marks
of the three other radiologists to render a final opinion. The goal of this process was
to identify as completely as possible all lung nodules in each CT scan without requiring forced consensus.

## Download
Follow the download instructions at [link](https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=1966254).

Then, the folder with raw downloaded data should contain folder `LIDC-IDRI`, which contains sub-folders `LIDC-IDRI-*`.
Example: `/path/to/the/downloaded/files/lidc/LIDC-IDRI/`.

## Usage
You can process the LIDC dataset using the
[`amid`](https://github.com/neuro-ml/amid/tree/master) library. Below is an example of how to use it:

```python
ds = LIDC(root='/path/to/the/downloaded/files/lidc/LIDC-IDRI/')
len(ds.ids)  # 1018
ds.image(ds.ids[0]).shape  # (512, 512, 194)
ds.cancer(ds.ids[0]).shape  # (512, 512, 194)
```

## Citation
if you found this dataset useful for your research, please cite:

```bibtex
@article{armato2011lung,
  title={The lung image database consortium (LIDC) and image database resource initiative (IDRI): a completed reference database of lung nodules on CT scans},
  author={Armato III, Samuel G and McLennan, Geoffrey and Bidaut, Luc and McNitt-Gray, Michael F and Meyer, Charles R and Reeves, Anthony P and Zhao, Binsheng and Aberle, Denise R and Henschke, Claudia I and Hoffman, Eric A and others},
  journal={Medical physics},
  volume={38},
  number={2},
  pages={915--931},
  year={2011},
  publisher={Wiley Online Library}
}
