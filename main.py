import os
import subprocess
import csv
import shutil
import json
import configparser
from biopandas.mol2 import PandasMol2
from biopandas.mol2 import split_multimol2

class molecule:
    def __init__(self,mol2_cont: str):
        self.mol2_cont = mol2_cont
    def show(self):
        print(self.mol2_cont)
        for each in self.mol2_cont:
            for e in each:
                if e[-1] == '\n':
                    print(e[:-1])
                else: print(e)


    def parser(Path):
        with open(Path, 'r') as f:
            count = 0
            Array = []
            for mol2 in split_multimol2(Path):
                count += 1
                Call = "molecule " + str(count)
                #mol2_id = mol2[0]
                mol2_cont = mol2[1:]
                Call = molecule(mol2_cont)
                Array.append(Call)
            return Array
            return Array
