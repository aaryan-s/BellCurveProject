import statistics
import csv
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
brand = []
rating = []
with open("BellCurveproject.csv", newline='') as csvfile:
    row = csv.DictReader(csvfile) #row 1
    for i in row:
        brand.append((i["Mobile Brand"]))
        rating.append(float(i["Avg Rating"]))
#print(brand)
#print(rating)

std = statistics.stdev(rating)
mean = statistics.mean(rating)
print("Rating mean:",mean)
median = statistics.median(rating)
print("Rating median:",median)
print("Standard Deviation for ratings:",std)


rating1start = mean - std
rating1end = mean + std
rating2start = rating1start - std
rating2end = rating1end + std
rating3start = rating2start - std
rating3end = rating2end + std



rating1stddev = [ i for i in rating if i < rating1end and i > rating1start]
rating2stddev = [ i for i in rating if i < rating2end and i > rating2start]
rating3stddev = [ i for i in rating if i < rating3end and i > rating3start]

fig = ff.create_distplot([rating3stddev],["Result"])
fig.show()