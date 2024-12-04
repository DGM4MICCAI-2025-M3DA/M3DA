import nibabel as nib
import numpy as np
# from amid.amos import AMOS
from connectome import Chain, Transform, Filter, CacheToRam
from deli import load_json

from ..amid.amos import AMOS
from ..config import PATH_AMOS22_RAW, PATH_AMOS22_LDCT, REPO_PATH
from ..const import LDCT_NOISE_INTENSITY, RANDOM_STATE
from ..utils import flatten


class FlipMRI(Transform):
    __inherit__ = True
    _mri_ids: tuple = tuple(flatten(load_json(REPO_PATH / "splits/Task02_CT_MR.json")[1:]))

    def image(id, image, _mri_ids):
        return np.flip(image, axis=0) if (id in _mri_ids) else image

    def mask(id, mask, _mri_ids):
        if mask is None:
            return None
        return np.flip(mask, axis=0) if (id in _mri_ids) else mask

    def affine(id, affine, _mri_ids):
        if id not in _mri_ids:
            return affine
        a = np.copy(affine)
        a[0][0] = -a[0][0]
        return a


class CTNoise(Transform):
    __inherit__ = True

    _apply_ids: tuple = tuple(flatten(load_json(REPO_PATH / "splits/Task03_CT_LDCT.json")[1:]))

    _noise_param: float = LDCT_NOISE_INTENSITY
    _hu_min: float = -1000
    _theta: int = 900
    _random_state: int = RANDOM_STATE

    def image(id, image, affine, _apply_ids, _noise_param, _hu_min, _theta, _random_state):
        if id not in _apply_ids:
            return image

        image_path = PATH_AMOS22_LDCT / f"{id}.nii.gz"

        if image_path.exists():
            return nib.load(str(image_path)).get_fdata()

        else:
            from ct_augmentation import simulate_ct_dose

            img = simulate_ct_dose(image, _noise_param, axes=(0, 1), random_state=_random_state, theta=_theta)
            img = np.clip(np.round(img, 0), image.min(), image.max())
            img[image <= _hu_min] = image[image <= _hu_min]

            img = img.astype(np.int16)
            nib.save(nib.Nifti1Image(img, affine=affine), image_path)
            return img


amos_base = Chain(
    AMOS(PATH_AMOS22_RAW),
    Filter(lambda id: int(id) <= 600),  # first AMOS data iteration!
    FlipMRI(),
    CacheToRam(('ids', ))
)
