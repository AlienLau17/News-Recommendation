import csv
import pandas as pd

pieces = []
s1 = pd.read_csv("2019_04_25_01_13h_entertainment.csv")
pieces.append(s1)
s2 = pd.read_csv("2019_04_25_15_22h_entertainment.csv")
pieces.append(s2)
newcsv = pd.concat(pieces, axis = 1)
newcsv.to_csv('2019_04_25_entertainment.csv')