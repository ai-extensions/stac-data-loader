Changes
==========

[Latest](https://gitlab.com/crim.ca/clients/terradue/stac-dataloader)
-------------------------------------------------------------------------------------------------------------

[//]: <> (Remove when new items added)
- No changes recorded yet.

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
