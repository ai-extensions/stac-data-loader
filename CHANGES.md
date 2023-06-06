Changes
==========

[Latest](https://gitlab.com/crim.ca/clients/terradue/stac-dataloader)
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
