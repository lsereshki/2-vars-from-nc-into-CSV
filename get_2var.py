import netCDF4 as nc
import csv

# Open the NetCDF file
nc_file = 'FWI_FENZ_NOV2022-MAY2023.nc'
dataset = nc.Dataset(nc_file)

#The variables' names (e.g. wspeed_noon or fwi) in the nc file are already known with ncdump commands
ws_noon = dataset.variables['wspeed_noon'][:]
FWI = dataset.variables['fwi'][:]

# Ensure the variables have the same length
if len(ws_noon) != len(FWI):
    raise ValueError("The two variables do not have the same length.")

# Open a CSV file for writing
csv_file = 'output.csv'
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header
    writer.writerow(['WindSpeed', 'FWI'])
    
    # Write the data
    for v1, v2 in zip(ws_noon, FWI):
        writer.writerow([v1, v2])

# Close the NetCDF file
dataset.close()
