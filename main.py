import os
import subprocess
import csv
import shutil
import json
import configparser
from biopandas.mol2 import PandasMol2
from biopandas.mol2 import split_multimol2

class molecule:
    def __init__(self,mol2_ID: list,mol2_ATOM: list,mol2_BOND: list,mol2_MAP: list):
        self.mol2_ID = mol2_ID
        self.mol2_ATOM = mol2_ATOM
        self.mol2_BOND = mol2_BOND
        self.mol2_MAP = mol2_MAP

    def show(self):
        Array = []
        Array.append(self.mol2_ID)
        Array.append(self.mol2_ATOM)
        Array.append(self.mol2_BOND)
        Array.append(self.mol2_MAP)
        return Array


    def parser(Path):
        with open(Path, 'r') as f:
            count = 0
            Array = []              #Собсна массив SnubArrayев, список всех молекул в файле
            for mol2 in split_multimol2(Path):
                count += 1
                SubArray = []       #SubArray - "раздел" (@MOLECULE, @ATOM, @BOND) содержащий в себе все строчки этого раздела.
                SnubArray = []      #SnubArray - list из нескольких (пока обычно трех) разделов, фактически - отдельная молекула
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
                    Call = molecule(SnubArray[0],SnubArray[1],SnubArray[2],SnubArray[2])
                    Array.append(Call)
            return Array
    def mapper(Map: list):
        SMAP = []
        for Bond in Map:
            Sym = []
            Sym = Bond.split()
            Aray = []
            Arrray = []
            Aray.append(Sym[1])
            Aray.append(Sym[2])
            Aray.append(Sym[3])
            Arrray.append(Sym[2])
            Arrray.append(Sym[1])
            Arrray.append(Sym[3])
            SMAP.append(Aray)
            SMAP.append(Arrray)
        print(SMAP)
