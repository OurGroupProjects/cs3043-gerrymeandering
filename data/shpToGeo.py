from os import listdir
import subprocess

srcFileName = "districtShapes/"
destFileName = "geo/"

for file in listdir("districtShapes"):
    if file[-4:] == ".shp":
        subprocess.check_output(['ogr2ogr', '-f', 'GeoJSON', '-t_srs', 'crs:84', destFileName + file[:-4] + '.json', srcFileName + file])
