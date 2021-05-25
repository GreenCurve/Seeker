import os
import subprocess
import csv
import shutil
import json
import configparser
from biopandas.mol2 import PandasMol2
from biopandas.mol2 import split_multimol2

Path = input("Введите путь к файлу: ") #C:\Users\Egor\Repo\input\ligands\mol2_F.mol2
Path = r"C:\Users\Egor\Repo\input\ligands\mol2_F.mol2" if Path == "" else Path
print(Path)
#pmol = PandasMol2().read_mol2(Path)
#Tsar = pmol.df[pmol.df['atom_type'] == 'C.ar']
#print('Molecule ID: %s' % pmol.code)
#print('\nRaw MOL2 file contents:\n\n%s\n...' % pmol.mol2_text)
#print('number of Russian Tsars: %d' % Tsar.shape[0])
with open(Path, 'r') as f:
    for mol2 in split_multimol2(Path):
        mol2_id = mol2[0]
        mol2_cont = mol2[1:]
        print('Molecule ID:\n', mol2_id)
        print('Content:\n')
        for each in mol2_cont:
            for e in each:
                print(e[:-1])
