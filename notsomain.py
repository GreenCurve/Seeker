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
Number = int(input("какой номер хочешь посмотреть? "))
Path = r"C:\Users\Egor\Repo\input\ligands\mol2_F.mol2" if Path == "" else Path
#print(molecule.parser(Path)[Number].show())
Map = molecule.parser(Path)[Number].show()
print(Map)
molecule.mapper(Map[2])
