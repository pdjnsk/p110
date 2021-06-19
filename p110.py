from main import random_set_of_mean, show_fig
import statistics
import plotly.figure_factory as ff
import pandas as pd
import csv

df = pd.read_csv('data.csv')

data = df["temp"].tolist()

mean = statistics.mean(data)
sd = statistics.stdev(data)

print(mean)
print(sd)


def plot_graph(meanList):
    df = meanList
    means = statistics.mean(df)
    fig = ff.create_distplot(df,["temp"], show_hist= False)
    fig.add_trace(x= [means,means], y= [0,1], mode= "lines", name = "mean" )
    fig.show()

def setup():
    meanList = []
    for i in range(0,100):
        set_of_mean = random_set_of_mean(100)
        meanList.append(set_of_mean)

    show_fig(meanList)
    mean = statistics.mean(meanList)
    print("mean of sample data", mean)
setup()

pmean = statistics.mean(data)
print("mean of population data", pmean)

def standardDeavtion():
    meanList = []
    for i in range(1,100):
       set_of_mean = random_set_of_mean(10)
       meanList.append(set_of_mean)

    std_deviation = statistics.stdev(meanList)
    print("Standard deviation of sample data:- ", std_deviation)

standardDeavtion()

sd = statistics.stdev(data)
print("standard devation of population data", sd)

