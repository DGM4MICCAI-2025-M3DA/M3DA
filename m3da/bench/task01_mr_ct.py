from connectome import Filter
from deli import load_json

from ..config import REPO_PATH
from ..datasets.amos import amos_base
from ..utils import flatten


labels_mr_ct = tuple(range(16))
background_lbl_mr_ct = 0

split_mr_ct = load_json(REPO_PATH / "splits/Task01_MR_CT.json")
dataset_mr_ct = amos_base >> Filter(lambda id: id in flatten(split_mr_ct))
spacing_mr_ct = (1.1875, 1.1875, 3.0)

split_mr_ct_oracle = load_json(REPO_PATH / "splits/Task01_MR_CT_oracle.json")
dataset_mr_ct_oracle = amos_base >> Filter(lambda id: id in flatten(split_mr_ct_oracle))
spacing_mr_ct_oracle = (0.663, 0.663, 5.0)
