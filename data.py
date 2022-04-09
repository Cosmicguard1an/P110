import statistics
import csv
import pandas as pd
import random
import plotly.figure_factory as ff

df = pd.read_csv('medium_data.csv')
popList = df['responses'].tolist()
popMean = statistics.mean(popList)

def randomMean(count):
    dataSet = []
    for i in range(0, count):
        random_i = random.randint(0,len(popList))
        val = popList[random_i]
        dataSet.append(val)
    mean = statistics.mean(dataSet)
    return mean

def plot(means):
    df = means
    fig = ff.create_distplot([df], ["Responses"],show_hist = False)
    fig.show()  


def setup():
    mean_list = []
    for i in range(0,100):
        setMeans = randomMean(30)
        mean_list.append(setMeans)
    plot(mean_list)
    sampleMean = statistics.mean(mean_list)
    print('Mean of 100 Samples: ',sampleMean)
    print('Mean of Population: ',popMean)

setup()



