from connectome import Filter
from deli import load_json

from ..config import REPO_PATH
from ..datasets.cc359 import cc359_base
from ..utils import flatten


labels_t1sc = tuple(range(4))
background_lbl_t1sc = 0

split_t1sc = load_json(REPO_PATH / "splits/Task07_T1Sc.json")
dataset_t1sc = cc359_base >> Filter(lambda id: id in flatten(split_t1sc))
spacing_t1sc = (1.0, 1.0, 1.0)

split_t1sc_oracle = load_json(REPO_PATH / "splits/Task07_T1Sc_oracle.json")
dataset_t1sc_oracle = cc359_base >> Filter(lambda id: id in flatten(split_t1sc_oracle))
spacing_t1sc_oracle = (1.00, 1.00, 1.33)
