import csv

# import pandas as pd

# pieces = []
# for num in [1, 2, 3]:
#     s = pd.read_csv('folder/subfolder/File%d.csv' % num) # your directory
#     pieces.append(s)
# newcsv = pd.concat(pieces, axis=1) # this will yield multiple columns
# newcsv.to_csv('folder/subfolder/newcsv.csv')


with open("2019_04_25_15_22h_sport.csv" , "r") as csvinput:
    r = csv.reader(csvinput)
    with open("2019_04_25_sport.csv", "w") as csvoutput:
        w = csv.writer(csvoutput)
        next(r, None)
        w.writerow(["url", "title", "description", "urlToImage", "date"])
        for row in csv.reader(csvinput):
            w.writerow(row + ["2019-04-25"])

with open("2019_04_26_12_22h_sport.csv" , "r") as csvinput:
    r = csv.reader(csvinput)
    with open("2019_04_26_sport.csv", "w") as csvoutput:
        w = csv.writer(csvoutput)
        next(r, None)
        w.writerow(["url", "title", "description", "urlToImage", "date"])
        for row in csv.reader(csvinput):
            w.writerow(row + ["2019-04-26"])

with open("2019_04_27_13_22h_sport.csv" , "r") as csvinput:
    r = csv.reader(csvinput)
    with open("2019_04_27_sport.csv", "w") as csvoutput:
        w = csv.writer(csvoutput)
        next(r, None)
        w.writerow(["url", "title", "description", "urlToImage", "date"])
        for row in csv.reader(csvinput):
            w.writerow(row + ["2019-04-27"])