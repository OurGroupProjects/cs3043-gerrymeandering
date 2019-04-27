from urllib import request
from zipfile import ZipFile
from multiprocessing import Pool

base_url = 'http://cdmaps.polisci.ucla.edu/shp/'
base_file_name = 'districts'
file_extension = '.zip'
num_padding = 3
last_district = 114
num_processes = 10

def getDistrictInfo(i):
    num = i+1
    file_name = base_file_name + str(num).rjust(num_padding, '0') + file_extension
    local_file_name, headers = request.urlretrieve(base_url+file_name)
    ZipFile(local_file_name, 'r').extractall()
    request.urlcleanup()
    return

if __name__ == "__main__":
    with Pool(processes=num_processes) as pool:
        [i for i in pool.imap_unordered(getDistrictInfo, range(last_district))]
