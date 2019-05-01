import csv


with open("2019_04_25_15_22h_health.csv" , "r") as csvinput:
    r = csv.reader(csvinput)
    with open("2019_04_25_health.csv", "w") as csvoutput:
        w = csv.writer(csvoutput)
        next(r, None)
        w.writerow(["url", "title", "description", "urlToImage", "date"])
        for row in csv.reader(csvinput):
            w.writerow(row + ["2019-04-25"])

with open("2019_04_26_12_22h_health.csv" , "r") as csvinput:
    r = csv.reader(csvinput)
    with open("2019_04_26_health.csv", "w") as csvoutput:
        w = csv.writer(csvoutput)
        next(r, None)
        w.writerow(["url", "title", "description", "urlToImage", "date"])
        for row in csv.reader(csvinput):
            w.writerow(row + ["2019-04-26"])

with open("2019_04_27_13_22h_health.csv" , "r") as csvinput:
    r = csv.reader(csvinput)
    with open("2019_04_27_health.csv", "w") as csvoutput:
        w = csv.writer(csvoutput)
        next(r, None)
        w.writerow(["url", "title", "description", "urlToImage", "date"])
        for row in csv.reader(csvinput):
            w.writerow(row + ["2019-04-27"])

with open("2019_04_28_13_22h_health.csv" , "r") as csvinput:
    r = csv.reader(csvinput)
    with open("2019_04_28_health.csv", "w") as csvoutput:
        w = csv.writer(csvoutput)
        next(r, None)
        w.writerow(["url", "title", "description", "urlToImage", "date"])
        for row in csv.reader(csvinput):
            w.writerow(row + ["2019-04-28"])