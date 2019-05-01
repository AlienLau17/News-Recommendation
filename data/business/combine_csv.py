import csv



with open("2019_business.csv", "w") as csvoutput:
    w = csv.writer(csvoutput)
    w.writerow(["url", "title", "description", "urlToImage", "date"])
    for num in range(24,31):
        try:
            with open("2019_04_"+str(num)+"_business.csv", "r") as csvinput:
                r = csv.reader(csvinput)
                next(r, None)
                for row in r:
                    w.writerow(row)
        except:
            pass