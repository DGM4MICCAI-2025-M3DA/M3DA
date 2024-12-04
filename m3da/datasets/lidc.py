import numpy as np
from amid.lidc import LIDC
from connectome import CacheToRam, Chain, Transform

from ..config import PATH_LIDC_RAW


class BuildMask(Transform):
    __inherit__ = True

    def mask(cancer):
        return np.int8(cancer)


lidc_base = Chain(
    LIDC(PATH_LIDC_RAW),
    BuildMask(),
    CacheToRam(('ids', ))
)
