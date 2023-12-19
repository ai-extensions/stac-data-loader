Changes
==========

[Latest](https://gitlab.com/crim.ca/clients/terradue/stac-dataloader)
-------------------------------------------------------------------------------------------------------------

[//]: <> (Remove when new items added)
- No changes recorded yet.

[0.5.0](https://gitlab.com/crim.ca/clients/terradue/stac-dataloader/-/tree/0.5.0) (2023-12-19)
-------------------------------------------------------------------------------------------------------------

- Add STAC Extension [`stats`](https://github.com/stac-extensions/stats) to `EuroSAT` results to provide a metric
  about the number of samples in the dataset.
- Add distinct `CATALOG_STAC_URL` and `CATALOG_DATA_URL` configuration options to allow referencing to distinct
  endpoints for STAC Catalog, Collections and Items, and their referenced STAC Assets since metadata and actual
  assets data are most often than not hosted by different servers (i.e.: STAC API endpoints vs cloud/data provider).
- Add more details guiding post-generation steps to upload and reference `EuroSAT` data to a server
  using the reference [STAC-populator](https://github.com/crim-ca/stac-populator) tool with `DirectoryLoader`.
- Fix `bbox` CRS calculation in `stac_eurosat` notebook causing STAC Collections and Items to report invalid geospatial
  locations.

[0.4.0](https://gitlab.com/crim.ca/clients/terradue/stac-dataloader/-/tree/0.4.0) (2023-11-09)
-------------------------------------------------------------------------------------------------------------

- Replace invalid STAC Collection `properties` by corresponding `summaries` definitions in `EuroSAT` notebook.
- Use an updated (patch) ML-AOI STAC Extension JSON schema to allow `ml-aoi` references in STAC Collections
  (relates to [stac-extensions/ml-aoi#5](https://github.com/stac-extensions/ml-aoi/issues/5)).
- Using the patched ML-AOI STAC Extension, allow ``ml-aoi`` used along other STAC Extensions to succeed JSON schema 
  validation (relates to [stac-extensions/ml-aoi#6](https://github.com/stac-extensions/ml-aoi/issues/6)).
- Add `rel: related` cross-reference links to STAC Collections for all other splits to highlight their relationship.
- Improve definitions with more fields fulfilling STAC Extensions `sci`, `file`, `raster` and `label`.
- Add STAC Asset `roles` with relevant values for each item.

[0.3.3](https://gitlab.com/crim.ca/clients/terradue/stac-dataloader/-/tree/0.3.3) (2023-06-06)
-------------------------------------------------------------------------------------------------------------

- Add the `EuroSAT100` subset as example with STAC definitions and associated imagery and annotation assets.
- Add the GitHub tag version as the `version` field for version control of STAC components.
- Use the published GitHub [ai-extensions/stac-data-loader](https://github.com/ai-extensions/stac-data-loader)
  location as the default base URL for the STAC components of the `EuroSAT100` subset example.
- Add progress bars rendering for the STAC Schema validation step of the STAC EuroSAT notebook. 

[0.3.2](https://gitlab.com/crim.ca/clients/terradue/stac-dataloader/-/tree/0.3.2) (2023-06-06)
-------------------------------------------------------------------------------------------------------------

- Fix invalid check of the `EuroSAT` subclass instance to decide between the `subset` or `full` data sub-directory.

[0.3.1](https://gitlab.com/crim.ca/clients/terradue/stac-dataloader/-/tree/0.3.1) (2023-05-30)
-------------------------------------------------------------------------------------------------------------

- Fix erroneously named sections in Markdown Cells of [`notebooks/stac_eurosat.ipynb`](notebooks/stac_eurosat.ipynb).
- Fix missing bump versioning of the [`stac_dataloader`](stac_dataloader) package in [`pyproject.toml`](pyproject.toml).
- Regroup and reuse common typing definitions in [`stac_dataloader/typedef.py`](stac_dataloader/typedef.py).
- Fix erroneous dependency packages.

[0.3.0](https://gitlab.com/crim.ca/clients/terradue/stac-dataloader/-/tree/0.3.0) (2023-05-30)
-------------------------------------------------------------------------------------------------------------

- Add notebook to convert [EuroSAT](https://github.com/phelber/EuroSAT) dataset obtained through
  [torchgeo.datasets.EuroSAT](https://torchgeo.readthedocs.io/en/stable/api/datasets.html#torchgeo.datasets.EuroSAT)
  into STAC Catalog, Collections, Items and Assets using the STAC [Label](https://github.com/stac-extensions/label)
  extension to provide annotated Land-Cover samples over Sentinel-2 imagery.

[0.2.0](https://gitlab.com/crim.ca/clients/terradue/stac-dataloader/-/tree/0.2.0) (2023-05-25)
-------------------------------------------------------------------------------------------------------------

- Add sample Notebook with STAC search and data loading using Land-Cover annotated data catalogued on
  [Microsoft Planetary Computer](https://planetarycomputer.microsoft.com/dataset) STAC dataset server,
  and provided through COG assets from NRCan's AWS servers. Use Landsat imagery as reference for training.
- Add sample data preparation, loading iterator and stacking of Landsat imagery and Land-Cover chips
  using `xbatcher` from [zen3geo](https://github.com/weiji14/zen3geo) utilities and `torchdata` Data-Pipes.
- Add [`leafmap`](https://github.com/opengeos/leafmap) for the visualization of samples during dataset preparation.

[0.1.0](https://gitlab.com/crim.ca/clients/terradue/stac-dataloader/-/tree/0.1.0) (2023-04-25)
-------------------------------------------------------------------------------------------------------------

- Initial setup of the repository.
- Initial implementation of STAC DataLoader using Radiant MLHub Python client.
