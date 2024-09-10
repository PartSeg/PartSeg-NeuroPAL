from __future__ import annotations
from enum import Enum, auto
from typing import TYPE_CHECKING
import numpy as np

if TYPE_CHECKING:
    from napari.layers import Image
    from npe2.types import LayerData


class CombineMode(Enum):
    add = auto()
    max = auto()


def combine_channels(channels: list[Image], mode: CombineMode) -> LayerData:
    if mode == CombineMode.add:
        return np.sum([channel.data for channel in channels], axis=0)
    elif mode == CombineMode.max:
        return np.max([channel.data for channel in channels], axis=0)
    else:
        raise ValueError(f"Invalid mode: {mode}")
