import os
import subprocess
import csv
import shutil
import json
import configparser
from biopandas.mol2 import PandasMol2
from biopandas.mol2 import split_multimol2
from main import molecule

Path = input("Введите путь к файлу: ") #C:\Users\Egor\Repo\input\ligands\mol2_F.mol2
Number = input("какой номер хочешь посмотреть?")
Path = r"C:\Users\Egor\Repo\input\ligands\mol2_F.mol2" if Path == "" else Path
def parser(Path):
    with open(Path, 'r') as f:
        for mol2 in split_multimol2(Path):
            mol2_id = mol2[0]
            mol2_cont = mol2[1:]
            molecule = molecule(mol2_id,mol2_cont)
