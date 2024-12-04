from amid.cc359 import CC359
from connectome import Chain, Transform, Filter, CacheToRam

from ..config import PATH_CC359_RAW


class BuildMask(Transform):
    __inherit__ = True

    def mask(wm_gm_csf):
        return wm_gm_csf


cc359_base = Chain(
    CC359(PATH_CC359_RAW),
    BuildMask(),
    Filter(lambda mask: mask is not None),
    CacheToRam(('ids', ))
)
