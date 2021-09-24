### Identifiers

| Relationship   | ID Type              | ID(s)                                                                                                                                            |
|:---------------|:---------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------|
| Root           | OSUKED ID            | 10294                                                                                                                                            |
| Related        | Settlement BMU ID    | T_ABRBO-1                                                                                                                                        |
| Related        | National Grid BMU ID | ABRBO-1                                                                                                                                          |
| Equivalent     | Common Name          | Aberdeen Bay                                                                                                                                     |
| Equivalent     | 4C-Offshore ID       | [aberdeen-(eowdc)-united-kingdom-uk47](https://www.4coffshore.com/windfarms/united-kingdom/aberdeen-(eowdc)-united-kingdom-uk47.html)            |
| Equivalent     | WindPowerNet ID      | [windfarm_en_16769_eowdc](https://www.thewindpower.net/windfarm_en_16769_eowdc.php)                                                              |
| Equivalent     | Wikidata ID          | [Q17509465](https://www.wikidata.org/wiki/Q17509465)                                                                                             |
| Equivalent     | Wikipedia ID         | [European_Offshore_Wind_Deployment_Centre](https://en.wikipedia.org/wiki/European_Offshore_Wind_Deployment_Centre)                               |
| Equivalent     | Power-Technology ID  | [european-offshore-wind-deployment-centre-aberdeen](https://www.power-technology.com/projects/european-offshore-wind-deployment-centre-aberdeen) |
| Equivalent     | EIC ID               | 48W00000ABRBO-19                                                                                                                                 |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | Value   |
|:------------|:--------|
| Fuel Type   | WIND    |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -1.97 |
| Latitude    |   57.22 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/wind-farms/datapackage.json">Wind Farms</a>

Dataset listing the plant types and hub-heights of wind farms

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   | Value    |
|:------------|:---------|
| Plant Type  | offshore |
| Hub-Height  | 120.0    |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |     Value |
|:--------------------|-------:|----------:|
| Annual Output (MWh) |   2016 |      0.00 |
| Annual Output (MWh) |   2017 |      0.00 |
| Annual Output (MWh) |   2018 |      0.00 |
| Annual Output (MWh) |   2019 | 290247.22 |
| Annual Output (MWh) |   2020 | 312950.56 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   Value |
|:----------------------|-------:|--------:|
| Capture Price (£/MWh) |   2019 |   39.43 |
| Capture Price (£/MWh) |   2020 |   32.76 |