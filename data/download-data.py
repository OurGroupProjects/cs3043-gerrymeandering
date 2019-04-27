from urllib import request
from zipfile import ZipFile

base_url = 'http://cdmaps.polisci.ucla.edu/shp/'
base_file_name = 'districts'
file_extension = '.zip'
num_padding = 3
last_district = 114

def getDistrictInfo(num):
    file_name = base_file_name + str(num).rjust(num_padding, '0') + file_extension
    local_file_name, headers = request.urlretrieve(base_url+file_name)
    ZipFile(local_file_name, 'r').extractall()
    request.urlcleanup()

for i in range(last_district):
    getDistrictInfo(i+1)
