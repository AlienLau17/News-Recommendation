import csv

with open("2019_04_24_03_6h_business.csv" , "r") as csvinput:
    r = csv.reader(csvinput)
    with open("2019_04_24_business.csv", "w") as csvoutput:
        w = csv.writer(csvoutput)
        next(r, None)
        w.writerow(["url", "title", "description", "urlToImage", "date"])
        for row in csv.reader(csvinput):
            w.writerow(row + ["2019-04-24"])

with open("2019_04_25_15_22h_business.csv" , "r") as csvinput:
    r = csv.reader(csvinput)
    with open("2019_04_25_business.csv", "w") as csvoutput:
        w = csv.writer(csvoutput)
        next(r, None)
        w.writerow(["url", "title", "description", "urlToImage", "date"])
        for row in csv.reader(csvinput):
            w.writerow(row + ["2019-04-25"])

with open("2019_04_26_12_22h_business.csv" , "r") as csvinput:
    r = csv.reader(csvinput)
    with open("2019_04_26_business.csv", "w") as csvoutput:
        w = csv.writer(csvoutput)
        next(r, None)
        w.writerow(["url", "title", "description", "urlToImage", "date"])
        for row in csv.reader(csvinput):
            w.writerow(row + ["2019-04-26"])

with open("2019_04_27_13_22h_business.csv" , "r") as csvinput:
    r = csv.reader(csvinput)
    with open("2019_04_27_business.csv", "w") as csvoutput:
        w = csv.writer(csvoutput)
        next(r, None)
        w.writerow(["url", "title", "description", "urlToImage", "date"])
        for row in csv.reader(csvinput):
            w.writerow(row + ["2019-04-27"])

with open("2019_04_28_13_22h_business.csv" , "r") as csvinput:
    r = csv.reader(csvinput)
    with open("2019_04_28_business.csv", "w") as csvoutput:
        w = csv.writer(csvoutput)
        next(r, None)
        w.writerow(["url", "title", "description", "urlToImage", "date"])
        for row in csv.reader(csvinput):
            w.writerow(row + ["2019-04-28"])

with open("2019_04_30_17_22h_business.csv" , "r") as csvinput:
    r = csv.reader(csvinput)
    with open("2019_04_30_business.csv", "w") as csvoutput:
        w = csv.writer(csvoutput)
        next(r, None)
        w.writerow(["url", "title", "description", "urlToImage", "date"])
        for row in csv.reader(csvinput):
            w.writerow(row + ["2019-04-30"])