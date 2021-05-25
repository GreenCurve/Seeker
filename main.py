import os
import subprocess
import csv
import shutil
import json
import configparser
from biopandas.mol2 import PandasMol2
from biopandas.mol2 import split_multimol2

class molecule:
    def __init__(self,mol2_id: str,mol2_cont: str):
        self.mol2_id = mol2_id
        self.mol2_cont = mol2_cont
    def show(self):
        for each in self.mol2_cont:
            for e in each:
                print(e[:-1])
