from typing import Any, Dict, List, Literal, Optional, Tuple, TypedDict, Union
from typing_extensions import NotRequired
from datetime import datetime

import torch

Split = Literal["train", "validate", "test"]

TemporalInterval = Tuple[
    Optional[datetime],
    Optional[datetime],
]

GeometryTypes = Literal["Point", "LineString", "Polygon", "MultiPoint", "MultiLineString", "MultiPolygon"]
Geometry = TypedDict("Geometry", {
    "type": GeometryTypes,
    "coordinates": List[Union[float, int]],
})
GeoFeature = TypedDict("GeoFeature", {
    "type": Literal["Feature"],
    "geometry": Geometry,
    "properties": NotRequired[Dict[str, Any]],
})
GeoFeatureCollection = TypedDict("GeoFeatureCollection", {
    "type": Literal["FeatureCollection"],
    "features": List[GeoFeature],
})
GeoJSON = Union[GeoFeatureCollection, GeoFeature]

# generic interface of torchgeo, but more explicit
GeoSample = TypedDict(
    "GeoSample",
    {
        "image": torch.Tensor,
        "label": torch.Tensor,
    },
    total=True,
)
