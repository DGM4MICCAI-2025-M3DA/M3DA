import numpy as np
from amid.brats2021 import BraTS2021
from connectome import Chain, Transform, Filter, CacheToRam

from ..config import PATH_BRATS2021_RAW


class BuildMask(Transform):
    __inherit__ = True

    def mask(mask):
        mask_new = np.copy(mask)
        mask_new[mask_new == 4] = 3
        return mask_new


brats_base = Chain(
    BraTS2021(PATH_BRATS2021_RAW),
    Filter(lambda fold: fold == 'TrainingData'),
    BuildMask(),
    CacheToRam(('ids', ))
)
