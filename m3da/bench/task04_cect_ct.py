from connectome import Filter
from deli import load_json

from ..config import REPO_PATH
from ..datasets.lidc import lidc_base
from ..utils import flatten


labels_cect_ct = (0, 1)
background_lbl_cect_ct = 0

split_cect_ct = load_json(REPO_PATH / "splits/Task04_ceCT_CT.json")
dataset_cect_ct = lidc_base >> Filter(lambda id: id in flatten(split_cect_ct))
spacing_cect_ct = (0.723, 0.723, 1.25)  # nnUNet recommendation is 2.5 instead of 1.25

split_cect_ct_oracle = load_json(REPO_PATH / "splits/Task04_ceCT_CT_oracle.json")
dataset_cect_ct_oracle = lidc_base >> Filter(lambda id: id in flatten(split_cect_ct_oracle))
spacing_cect_ct_oracle = spacing_cect_ct
