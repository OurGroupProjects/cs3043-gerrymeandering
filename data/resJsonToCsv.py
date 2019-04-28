import sys
import json
import csv
from pprint import pprint

json_file_in = 'res/districtsData.json'
csv_file_out = 'res/districtsData.csv'

columns = [
    'state',
    'start_cong',
    'end_cong',
    'district_num',
    'area',
    'perimeter',
    'max_from_center',
]

total_congresses = 114
total_districts = 435 * total_congresses

with open(csv_file_out, 'w+', newline='') as fout:
    csv_out = csv.writer(fout)
    csv_out.writerow(columns)
    with open(json_file_in) as fin:
        json_data = json.loads(fin.read())

    for congress in json_data:
        for district in congress:
            row = [
                district['properties']['STATENAME'], # State
                district['properties']['STARTCONG'],
                district['properties']['ENDCONG'],
                district['properties']['DISTRICT'],  # District number
                district['computedStats']['area'],   # Computed vals
                district['computedStats']['perimeter'],
                district['computedStats']['maxFromCenter'],
            ]
            csv_out.writerow(row)
