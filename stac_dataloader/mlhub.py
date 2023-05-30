from typing import Any, Callable, Dict, List, Optional, Sequence, Union

from rasterio.crs import CRS
from torchgeo.datasets import BoundingBox
from radiant_mlhub import Dataset, DownloadIfExistsOpts

from stac_dataloader.generic import STACDataset
from stac_dataloader.typedef import GeoJSON, GeoSample, TemporalInterval


class MLHubDataset(STACDataset):
    def __init__(
        self,
        mlhub_dataset: Union[str, List[str]],
        mlhub_api_key: Optional[str] = None,
        root: str = "data",
        crs: Optional[CRS] = None,
        res: Optional[float] = None,
        bands: Optional[Sequence[str]] = None,
        intersects_bbox: Optional[BoundingBox] = None,
        intersects_geojson: Optional[GeoJSON] = None,
        intersects_interval: Optional[TemporalInterval] = None,
        collection_filter: Optional[List[str]] = None,
        validate_assets: bool = False,
        transforms: Optional[Callable[[Dict[str, Any]], Dict[str, Any]]] = None,
        cache: bool = True,
    ) -> None:
        """Initialize a new Dataset instance.

        Args:
            mlhub_dataset:
                One or more Dataset IDs or DOIs to retrieve from Radiant MLHub collections.
            mlhub_api_key:
                API key provided from Radiant MLHub (https://mlhub.earth) user registration.
                This can also be specified using ``MLHUB_API_KEY`` environment variable or configured
                in ``~/.mlhub/profiles``.
            root:
                Root directory where dataset can be found. If it does not exist,
                it will be used to download and cache data.
            crs:
                :term:`coordinate reference system (CRS)` to warp to
                (defaults to the CRS of the first file found)
            res:
                resolution of the dataset in units of CRS
                (defaults to the resolution of the first file found)
            bands:
                Bands to return (defaults to all bands)
            intersects_bbox:
                Only items that intersect these coordinates/date-times will be selected from the MLHub Collections.
                Area-of-Interest (AOI) coordinates are assumed in CRS EPSG:4326 unless ``crs`` is specified.
                Time-of-Interest (TOI) date-times must be provided using UTC-0 timestamp values.
            intersects_geojson: Alternate method to specify one or multiple Area-of-Interest (AOI)
            using GeoJSON coordinates.
                Only items that intersect these coordinates will be selected from the MLHub Collections.
            intersects_interval:
                Alternate method to ``intersects_bbox`` to specify Time-of-Interest (TOI) using a date-time range.
                Only items that intersect this date-time interval will be selected from the MLHub Collections.
            collection_filter:
                Explicit list of collection IDs to ignore (won't be downloaded).
                Each MLHub dataset can be composed of multiple STAC Collections.
                Those will be ignored if IDs are matched.
            validate_assets:
                If assets have already been downloaded and cached, re-validate their contents.
                This causes multiple requests to be sent to the MLHub server to compare authenticity of assets.
                This can slow down the initialization depending on the dataset size.
                If assets were already downloaded, validated and cached, it is faster to leave this disabled.
            transforms:
                Function/transform that takes an input sample and returns a transformed version.
            cache:
                if True, cache file handle to speed up repeated sampling.

        Raises:
            FileNotFoundError: if no files are found in ``root``
        """
        self.mlhub_dataset = mlhub_dataset
        self.mlhub_api_key = mlhub_api_key
        self.dataset = None
        super().__init__(
            root=root,
            crs=crs,
            res=res,
            bands=bands,
            intersects_bbox=intersects_bbox,
            intersects_geojson=intersects_geojson,
            intersects_interval=intersects_interval,
            collection_filter=collection_filter,
            validate_assets=validate_assets,
            transforms=transforms,
            cache=cache,
        )

    def prepare_dataset(self) -> None:
        self.dataset = Dataset.fetch(self.mlhub_dataset, api_key=self.mlhub_api_key)
        self.dataset.download(
            self.path,
            catalog_only=False,
            if_exists=DownloadIfExistsOpts.resume if self.validate_assets else DownloadIfExistsOpts.skip,
            collection_filter=self.collection_filter,
            **self.intersects,
        )

    def __getitem__(self, query: BoundingBox) -> GeoSample:
        """Retrieve image/mask and metadata indexed by query.

        Args:
            query: (minx, maxx, miny, maxy, mint, maxt) coordinates to index

        Returns:
            sample of image/mask and metadata at that index

        Raises:
            IndexError: if query is not found in the index
        """
