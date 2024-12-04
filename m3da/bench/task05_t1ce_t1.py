from connectome import Filter
from deli import load_json

from ..config import REPO_PATH
from ..datasets.brats import brats_base
from ..utils import flatten


labels_t1ce_t1 = tuple(range(4))
background_lbl_t1ce_t1 = 0

split_t1ce_t1 = load_json(REPO_PATH / "splits/Task05_T1ce_T1.json")
dataset_t1ce_t1 = brats_base >> Filter(lambda id: id in flatten(split_t1ce_t1))
spacing_t1ce_t1 = (1.0, 1.0, 1.0)

split_t1ce_t1_oracle = load_json(REPO_PATH / "splits/Task05_T1ce_T1_oracle.json")
dataset_t1ce_t1_oracle = brats_base >> Filter(lambda id: id in flatten(split_t1ce_t1_oracle))
spacing_t1ce_t1_oracle = spacing_t1ce_t1
