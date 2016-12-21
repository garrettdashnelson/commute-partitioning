# Commute partitioning automation script

## About

This set of scripts simplifies the process of running the [Combo](http://senseable.mit.edu/community_detection/) community-detection algorithm (developed by [Sobolevsky et all](http://journals.aps.org/pre/abstract/10.1103/PhysRevE.90.012811)) using commuter-flow data from the American Community Survey (ACS) in order to produce algorithmically-evaluated regionalizations of the United States. It is based on the process used by Nelson and Rae in the 2016 article ["A New Economic Geography of the United States: From Commutes to Megaregions"](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0166083). 

## Selecting extracts and running

The source file `data-src/commutes.csv` is a CSV file containing commuter flows between US Census Tracts derived from the ACS. **You will need to [download this file separately](https://www.dropbox.com/s/x5xz9v8ss6qyr0o/commutes.csv?dl=0) and place it in `data-src`, since it is too large for GitHub.** This file has been scrubbed to remove ultra-long-distance commutes, commutes with origins or destinations outside of the Lower 48 states, and commutes for which the origin and destination lie in the same Census tract. Tracts are identified by their 10-digit FIPS code.

The file `data-src/subselection.txt` is a listing of Census tracts, one per line, by FIPS code. **Modify this file to include the FIPS codes of the Census tracts which you wish to analyze.** The example selection is all of the Census tracts in the states of New Hampshire and Vermont. The Census Bureau has gazeteer files for 2010 Census tracts [available here](https://www.census.gov/geo/maps-data/data/gazetteer2010.html). *Note: if the file `data-src/subselection.txt` is removed, the script will operate on all available tract-to-tract commute data.*

**Run the preprocessor script.**

`$ python combo-preprocessor.py`

The result of this script is two files: `data-stage1/commutes.net`, a Pajek network file suitable for input into Combo, and `data-stage1/fips_table.csv`, a lookup table which will be used later to match FIPS codes to the serialized id numbers required by Combo. The examples included here are for the New Hampshire

**Run Combo.**

`$ ./comboCPP ./data-stage1/commutes.net [max-communities]`

The build of Combo included here is compiled for OS X. If it does not run correctly, you will have to [download the Combo source code](http://senseable.mit.edu/community_detection/combo.zip) and compile it yourself.

The variables [max-communities] may be left blank; if provided, Combo will limit to a given number of detected output communities.

The result of running Combo is a file, `data-stage1/commutes_comm_comboC++.txt`, with community assignments whose line numbers match the serialized ids in the Pajek file. Combo also writes the "modularity score" of the partitioning process to stdout.

**Reassemble the tracts lookup table**

`$ python combo-postprocessor.py`

The result of this script is `data-final/fips_table_with_community_assignments.csv`, which is a CSV file containing the FIPS codes of the input Census tracts, the serial id produced for Combo (which is useful only for debugging purposes), and, most usefully, the detected-communtiy id (community numbering begins at 0). 

You can now take this CSV file and join it to a spatial file of Census tracts or the [point-to-point flows Shapefile](https://figshare.com/articles/United_States_Commutes_and_Megaregions_data_for_GIS/4110156) used in our mapping.

## Contact information

Garrett Dash Nelson — garrett.g.d.nelson@dartmouth.edu · [@en_dash](http://www.twitter.com/en_dash) · http://people.matinic.us/garrett

Alasdair Rae — a.j.rae@sheffield.ac.uk · [@undertheraedar](http://twitter.com/undertheraedar) · http://statsmapsnpix.com

