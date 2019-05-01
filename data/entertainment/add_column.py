import csv

# import pandas as pd

# pieces = []
# for num in [1, 2, 3]:
#     s = pd.read_csv('folder/subfolder/File%d.csv' % num) # your directory
#     pieces.append(s)
# newcsv = pd.concat(pieces, axis=1) # this will yield multiple columns
# newcsv.to_csv('folder/subfolder/newcsv.csv')

with open("2019_04_24_03_6h_entertainment.csv" , "r") as csvinput:
    r = csv.reader(csvinput)
    with open("2019_04_24_entertainment.csv", "w") as csvoutput:
        w = csv.writer(csvoutput)
        next(r, None)
        w.writerow(["url", "title", "description", "urlToImage", "date"])
        for row in csv.reader(csvinput):
            w.writerow(row + ["2019-04-24"])

with open("2019_04_25_22h_entertainment.csv" , "r") as csvinput:
    r = csv.reader(csvinput)
    with open("2019_04_25_entertainment.csv", "w") as csvoutput:
        w = csv.writer(csvoutput)
        next(r, None)
        w.writerow(["url", "title", "description", "urlToImage", "date"])
        for row in csv.reader(csvinput):
            w.writerow(row + ["2019-04-25"])

with open("2019_04_26_12_22h_entertainment.csv" , "r") as csvinput:
    r = csv.reader(csvinput)
    with open("2019_04_26_entertainment.csv", "w") as csvoutput:
        w = csv.writer(csvoutput)
        next(r, None)
        w.writerow(["url", "title", "description", "urlToImage", "date"])
        for row in csv.reader(csvinput):
            w.writerow(row + ["2019-04-26"])

with open("2019_04_27_13_22h_entertainment.csv" , "r") as csvinput:
    r = csv.reader(csvinput)
    with open("2019_04_27_entertainment.csv", "w") as csvoutput:
        w = csv.writer(csvoutput)
        next(r, None)
        w.writerow(["url", "title", "description", "urlToImage", "date"])
        for row in csv.reader(csvinput):
            w.writerow(row + ["2019-04-27"])

with open("2019_04_28_13_22h_entertainment.csv" , "r") as csvinput:
    r = csv.reader(csvinput)
    with open("2019_04_28_entertainment.csv", "w") as csvoutput:
        w = csv.writer(csvoutput)
        next(r, None)
        w.writerow(["url", "title", "description", "urlToImage", "date"])
        for row in csv.reader(csvinput):
            w.writerow(row + ["2019-04-28"])

with open("2019_04_30_17_22h_entertainment.csv" , "r") as csvinput:
    r = csv.reader(csvinput)
    with open("2019_04_30_entertainment.csv", "w") as csvoutput:
        w = csv.writer(csvoutput)
        next(r, None)
        w.writerow(["url", "title", "description", "urlToImage", "date"])
        for row in csv.reader(csvinput):
            w.writerow(row + ["2019-04-30"])