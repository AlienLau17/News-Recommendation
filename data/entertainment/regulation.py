import csv
import re

# 2019_04_26[0-9a-zA-Z\_]+entertainment.csv
path = r'2019_04_26[0-9a-zA-Z\]+entertainment.csv'

with open(path , "r") as csvinput:
    r = csv.reader(csvinput)
    with open('2019_04_26_entertainment1.csv', "w") as csvoutput:
        w = csv.writer(csvoutput)
        next(r, None)
        w.writerow(["url", "title", "description", "urlToImage", "date"])
        for row in csv.reader(csvinput):
            w.writerow(row + ["2019-04-26"])