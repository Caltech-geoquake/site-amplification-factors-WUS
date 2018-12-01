# site-amplification-factors-WUS
##### Response spectra based site amplification factors for the western US.



### Data

The amplification factors are stored in the `data` folder as CSV files.



### Data format

Below is a brief explanation of the file names and file format.

1. The first number in a CSV file name means the Vs30 value (in m/s), and the second number means the z1000 value (in m).
2. The CSV files with names such as `175_008_period.csv` contains 240 reference period (in sec) in a single column.
3. The CSV files with names such as `175_008_af_rs_nl_hh_avg.csv` contains the mean nonlinear amplification factors. Each file has 11 rows and 240 columns. Each row corresponds to the amplification factors of a specific PGA, in the following order: 0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.75, 1.0, 1.25, 1.5 (unit: g).
4. The CSV files with names such as `175_008_af_rs_nl_hh_std.csv` contains the standard deviation of nonlinear amplification factors. The file format is the same as above (11 by 240).



### How to query

`Query.py` demonstrates how to query a site amplification factor corresponding to a (Vs30, z1000, PGA) combination. 

Currently, only a discrete set of combinations are supported. We are working on an interpolation scheme right now, which will support a range of Vs30, z1000, and PGA values.

