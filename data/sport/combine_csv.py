import csv


# with open("2019_04_24_03_6h_entertainment.csv" , "r") as csvinput:
#     r = csv.reader(csvinput)
#     with open("2019_04_24_entertainment.csv", "w") as csvoutput:
#         w = csv.writer(csvoutput)
#         next(r, None)
#         w.writerow(["url", "title", "description", "urlToImage", "date"])
#         for row in csv.reader(csvinput):
#             w.writerow(row + ["2019-04-24"])

with open("2019_sport.csv", "w") as csvoutput:
    w = csv.writer(csvoutput)
    w.writerow(["url", "title", "description", "urlToImage", "date"])
    for num in range(25, 31):
        try:
            with open("2019_04_"+str(num)+"_sport.csv", "r") as csvinput:
                r = csv.reader(csvinput)
                next(r, None)
                for row in r:
                    w.writerow(row)
        except:
            pass

#     with open("2019_04_24_entertainment.csv", "r") as csvinput:
#         r = csv.reader(csvinput)
#         for row in r:
#             w.writerow(row)

# with open("2019_entertainment.csv", "w") as csvoutput:    
#     for num in (25, 27):
#         with open("2019_04_"+str(num)+"_entertainment.csv", "r") as csvinput:
#             r = csv.reader(csvinput)
#             next(r, None)
#             for row in r:
#                 w.writerow(row)

# category = ['sports', 'entertainment']
# time = '2019'
# for i in range(len(category)):
#     file = time + category[i]+'.csv'
