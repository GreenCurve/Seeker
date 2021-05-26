import os
import subprocess
import csv
import shutil
import json
import configparser
from biopandas.mol2 import PandasMol2
from biopandas.mol2 import split_multimol2

class molecule:
    def __init__(self,mol2_cont: list):
        self.mol2_cont = mol2_cont
    def show(self):
        print(self.mol2_cont)


    def parser(Path):
        with open(Path, 'r') as f:
            count = 0
            Array = []
            for mol2 in split_multimol2(Path):
                count += 1
                SubArray = []
                SnubArray = []
                mol2_c = mol2[1:]
                for line in mol2_c:
                    for Each in line:
                        if line[-1] == Each:
                            SubArray.append(Each[:-1] if Each[-1:] == '\n' else Each)
                            SnubArray.append(SubArray)
                            SubArray = []
                        elif Each[:1] != '@':
                            SubArray.append(Each[:-1] if Each [-1:] == '\n' else Each)
                        elif SubArray == []: pass
                        else:
                            SnubArray.append(SubArray)
                            SubArray = []
                    Call = 'molecule' + str(count)
                    Call = molecule(SnubArray)
                    Array.append(Call)
            return Array
            return Array
