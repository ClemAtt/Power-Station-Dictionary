### Identifiers

| Relationship   | ID Type              | ID(s)                              |
|:---------------|:---------------------|:-----------------------------------|
| Root           | OSUKED ID            | 10021                              |
| Related        | Settlement BMU ID    | T_BAGE-1, T_BAGE-2                 |
| Related        | National Grid BMU ID | BAGE-1, BAGE-2                     |
| Related        | EIC ID               | 48W000000BAGE-1L, 48W000000BAGE-2J |
| Equivalent     | GPPD ID              | GBR1000312                         |
| Equivalent     | ESAIL ID             | BAGE                               |
| Equivalent     | Common Name          | Baglan Bay                         |
| Equivalent     | EUTL ID              | 96786                              |

<br>
### Linked Datasets
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/bmu-fuel-types/datapackage.json">Bmu Fuel Types</a>

Dataset published by Elexon describing the fuel types of the Balancing Mechanism Units (BMUs) that they process market settlement for. This dataset was retrieved from Elexon at 2021-08-09

The "ngc_bmu_id" field was used to match from the dictionary to the "NGC_BMU_ID" field in this dataset.

| Attribute   | BAGE-1   | BAGE-2   |
|:------------|:---------|:---------|
| Fuel Type   | CCGT     | CCGT     |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/plant-locations/datapackage.json">Plant Locations</a>

Dataset listing the locations of power plants

The "osuked_id" field was used to match from the dictionary to the "osuked_id" field in this dataset.

| Attribute   |   Value |
|:------------|--------:|
| Longitude   |   -5.03 |
| Latitude    |   51.72 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/global-power-plant-database/datapackage.json">Global Power Plant Database</a>

The Global Power Plant Database is a comprehensive, open source database of power plants around the world. It centralizes power plant data to make it easier to navigate, compare and draw insights for one’s own analysis. The database covers approximately 35,000 power plants from 167 countries and includes thermal plants (e.g. coal, gas, oil, nuclear, biomass, waste, geothermal) and renewables (e.g. hydro, wind, solar). Each power plant is geolocated and entries contain information on plant capacity, generation, ownership, and fuel type. It will be continuously updated as data becomes available. 

The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](https://www.wri.org/research/global-database-power-plants). Data updates may occur without associated updates to this manuscript.

The "gppd_idnr" field was used to match from the dictionary to the "gppd_idnr" field in this dataset.

| Attribute                           | Value                                                                          |
|:------------------------------------|:-------------------------------------------------------------------------------|
| Installed Capacity (MW)             | 520.0                                                                          |
| Longitude                           | -3.8352                                                                        |
| Latitude                            | 51.6145                                                                        |
| Primary Fuel Type                   | Gas                                                                            |
| Owner                               | MPF Operations Limited                                                         |
| Source                              | Department for Business Energy & Industrial Strategy                           |
| URL                                 | https://www.gov.uk/government/collections/digest-of-uk-energy-statistics-dukes |
| Geolocation Source                  | GEODB                                                                          |
| Estimated Annual Generation in 2017 | 2412.83                                                                        |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/verified-emissions/datapackage.json">Verified Emissions</a>

This dataset reports verified emissions within the EUTL. The EU Emissions Trading System (ETS) is a central instrument of the EU's policy to fight climate change and achieve cost-efficient reductions of greenhouse gas emissions. It is the world's biggest carbon market.

The "eutl_id" field was used to match from the dictionary to the "account_id" field in this dataset.

| Attribute              |   Year |      Value |
|:-----------------------|-------:|-----------:|
| CO2 Emissions (Tonnes) |   2005 | 1104318.00 |
| CO2 Emissions (Tonnes) |   2006 | 1142501.00 |
| CO2 Emissions (Tonnes) |   2007 | 1404009.00 |
| CO2 Emissions (Tonnes) |   2008 |  730296.00 |
| CO2 Emissions (Tonnes) |   2009 |  301470.00 |
| CO2 Emissions (Tonnes) |   2010 | 1205780.00 |
| CO2 Emissions (Tonnes) |   2011 | 1152511.00 |
| CO2 Emissions (Tonnes) |   2012 |  605184.00 |
| CO2 Emissions (Tonnes) |   2013 |  288263.00 |
| CO2 Emissions (Tonnes) |   2014 |  619573.00 |
| CO2 Emissions (Tonnes) |   2015 |  405240.00 |
| CO2 Emissions (Tonnes) |   2016 |  900350.00 |
| CO2 Emissions (Tonnes) |   2017 |  532621.00 |
| CO2 Emissions (Tonnes) |   2018 |  349518.00 |
| CO2 Emissions (Tonnes) |   2019 |  339161.00 |
| CO2 Emissions (Tonnes) |   2020 |   25023.00 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/annual-output/datapackage.json">Annual Output</a>

Total annual production of individual transmission level power plants on the GB power system

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute           |   Year |     BAGE-1 |   BAGE-2 |
|:--------------------|-------:|-----------:|---------:|
| Annual Output (MWh) |   2016 | 2360323.80 |  1520.71 |
| Annual Output (MWh) |   2017 | 1390345.30 |  1618.35 |
| Annual Output (MWh) |   2018 |  916399.95 |   607.71 |
| Annual Output (MWh) |   2019 |  890141.60 |  2722.05 |
| Annual Output (MWh) |   2020 |   59484.00 |  2289.95 |

<br><br>
##### <a href="https://raw.githubusercontent.com/OSUKED/Dictionary-Datasets/main/datasets/capture-prices/datapackage.json">Capture Prices</a>

This dataset reports the average price weighted by output that would have been received by the balancing mechanisms unit if it had participated fully in the day-ahead market. The price data used was sourced from Electric Insights

The "ngc_bmu_id" field was used to match from the dictionary to the "ngc_bmu_id" field in this dataset.

| Attribute             |   Year |   BAGE-1 |   BAGE-2 |
|:----------------------|-------:|---------:|---------:|
| Capture Price (£/MWh) |   2016 |    40.90 |    95.29 |
| Capture Price (£/MWh) |   2017 |    47.91 |    84.90 |
| Capture Price (£/MWh) |   2018 |    55.53 |    63.53 |
| Capture Price (£/MWh) |   2019 |    49.24 |    69.54 |
| Capture Price (£/MWh) |   2020 |    37.35 |    49.54 |