import sys
import os
import subprocess
from multiprocessing import Pool

last_district = 114
num_processes = 10
num_padding = 3
srcFileName = "geo\districts"
destFileName = "topo\districts"


def genTopo(i):
    num = i+1
    subprocess.check_output(['geo2topo', '-o', destFileName + str(num).rjust(num_padding, '0') + '.json', srcFileName + str(num).rjust(num_padding, '0') + '.json'], shell=True)


if __name__ == "__main__":
    genTopo(1)
    with Pool(processes=num_processes) as pool:
        [i for i in pool.imap_unordered(genTopo, range(last_district))]