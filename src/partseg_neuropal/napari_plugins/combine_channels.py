from enum import Enum, auto
from typing import TYPE_CHECKING, Annotated
import numpy as np

if TYPE_CHECKING:
    import napari
    import napari.types


class CombineMode(Enum):
    add = auto()
    max = auto()


def combine_channels(
    channels: Annotated[list["napari.layers.Image"], {"layout": "vertical"}],
    mode: CombineMode,
) -> "napari.types.LayerDataTuple":
    if mode == CombineMode.add:
        res = np.sum([channel.data for channel in channels], axis=0)
    elif mode == CombineMode.max:
        res = np.max([channel.data for channel in channels], axis=0)
    else:
        raise ValueError(f"Invalid mode: {mode}")
    print(f"Combined {len(channels)} channels with mode {mode}")
    return res, {"name": "Combined", "scale": channels[0].scale}, "image"
