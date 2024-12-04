from connectome import Filter
from deli import load_json

from ..config import REPO_PATH
from ..datasets.amos import amos_base
from ..utils import flatten


labels_ct_mr = tuple(range(16))
background_lbl_ct_mr = 0

split_ct_mr = load_json(REPO_PATH / "splits/Task02_CT_MR.json")
dataset_ct_mr = amos_base >> Filter(lambda id: id in flatten(split_ct_mr))
spacing_ct_mr = (0.663, 0.663, 5.0)

split_ct_mr_oracle = load_json(REPO_PATH / "splits/Task02_CT_MR_oracle.json")
dataset_ct_mr_oracle = amos_base >> Filter(lambda id: id in flatten(split_ct_mr_oracle))
spacing_ct_mr_oracle = (1.1875, 1.1875, 3.0)
