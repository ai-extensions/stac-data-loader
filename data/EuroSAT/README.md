# EuroSAT STAC Datasets

See the [STAC EuroSAT Jupyter Notebook][stac_eurosat_nb] to generate the contents of this directory.

## Dataset Variants

Following is the composition of each available dataset.

| Variant  | Class Name   | Train Samples   | Valid Samples   | Test Samples    | Total Samples | 
|----------|--------------|-----------------|-----------------|-----------------|---------------|
| `full`   | `EuroSAT`    | 16200 (60%)     | 5400 (20%)      | 5400 (20%)      | 27000         |
| `subset` | `EuroSAT100` | 60 <sup>1</sup> | 20 <sup>1</sup> | 20 <sup>1</sup> | 100           |

<sup>1</sup>  10 samples/class, 6 for training, 2 for validation and 2 for testing. No overlap between classes/splits.

**Note** <br>
The contents of the `full` variant are not included in the directory because of the generated data size. <br>
Refer to the [notebook][stac_eurosat_nb] and the various control options it provides to generate it locally.

In order to generate the contents of the offered `subset` variant, the

[stac_eurosat_nb]: ../../notebooks/stac_eurosat.ipynb

## Data Structure

Each [Dataset Variant](#dataset-variants) will have a `data/<variant>` and `stac/<variant>` subdirectories.
Under the `data` directory, a deeply nested structure is defined.
This is a result of the original ZIP data.
It is left as is to allow parsing and sample loading using the corresponding PyTorch data-loader.

When navigating down the `data/<variant>` hierarchy until the `sentinel_2` directory, 3 subdirectories will be defined:
- `label`: GeoJSON FeatureCollection of each sample
- `png`: RGB thumbnails of the corresponding imagery
- `tif`: Sentinel-2 GeoTiff imagery with all 13 bands

Under each of those directories, samples are categorized by their respective class (10) from the `EuroSAT` annotations.

Under the `stac/<variant>` directory, the STAC Collections and Items will be defined.
Those refer to the relevant files from the `data/<variant>` contents as STAC Assets.

They are categorized according to their dataset split:
- [STAC Collection `train`](stac/subset/train/collection.json)
- [STAC Collection `validate`](stac/subset/validate/collection.json)
- [STAC Collection `test`](stac/subset/test/collection.json)

A [STAC Catalog](stac/subset/catalog.json) that combines all the STAC Collections per split
is defined at the root of the `stac/<variant>` directory.

**Note** <br>
The `validate` split name is used instead of the original `valid` from `EuroSAT` to align with
[STAC ML-AOI](https://github.com/stac-extensions/ml-aoi#item-properties-and-collection-fields) annotation format.
