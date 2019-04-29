import csv 



with open("2019_health.csv", "w") as csvoutput:
    w = csv.writer(csvoutput)
    w.writerow(["url", "title", "description", "urlToImage", "date"])
    for num in (25, 27):
        with open("2019_04_"+str(num)+"_health.csv", "r") as csvinput:
            r = csv.reader(csvinput)
            next(r, None)
            for row in r:
                w.writerow(row)