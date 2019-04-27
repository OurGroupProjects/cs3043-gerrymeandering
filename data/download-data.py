from urllib import request
from zipfile import ZipFile

base_url = 'http://cdmaps.polisci.ucla.edu/shp/'
base_file_name = 'districts'
file_extension = '.zip'
num_padding = 3
last_district = 114

for i in range(last_district):
    num = i+1
    file_name = base_file_name + str(num).rjust(num_padding, '0') + file_extension
    local_file_name, headers = request.urlretrieve(base_url+file_name)
    with ZipFile(local_file_name, 'r') as zipfile:
        zipped_files = zipfile.namelist()
        for f in zipped_files:
            if f.endswith('.shp'):
                zipfile.extract(f, 'shp')
    request.urlcleanup()
