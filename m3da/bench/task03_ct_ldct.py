from connectome import Filter
from deli import load_json

from ..config import REPO_PATH
from ..datasets.amos import amos_base, CTNoise
from ..utils import flatten


labels_ct_ldct = tuple(range(16))
background_lbl_ct_ldct = 0

split_ct_ldct = load_json(REPO_PATH / "splits/Task03_CT_LDCT.json")
dataset_ct_ldct = amos_base >> Filter(lambda id: id in flatten(split_ct_ldct)) >> CTNoise()
spacing_ct_ldct = (0.663, 0.663, 5.0)

split_ct_ldct_oracle = load_json(REPO_PATH / "splits/Task03_CT_LDCT_oracle.json")
dataset_ct_ldct_oracle = amos_base >> Filter(lambda id: id in flatten(split_ct_ldct_oracle)) \
                         >> CTNoise(apply_ids=tuple(flatten(split_ct_ldct_oracle)))
spacing_ct_ldct_oracle = spacing_ct_ldct
