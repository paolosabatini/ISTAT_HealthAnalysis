import numpy as np
import matplotlib.pyplot as plt


def plotGeoWeights(geo_weights):
    x_values = np.arange(1, len(geo_weights.keys()) + 1, 1)
    plt.figure()
    
    plt.bar(x_values,geo_weights.values(),align="center")
    plt.xticks(x_values, geo_weights.keys())
    plt.xlabel('Interviewer geographic location')
    plt.ylabel('Geographic weight')
    axes = plt.gca() # get current axes
    axes.set_ylim([0,2])
    plt.savefig("plots/geo_weights.png")

def plotGeoSmoke(geo_smoke):
    plt.figure()
    x_values = np.arange(1, len(geo_smoke.keys()) + 1, 1)
    plt.bar(x_values,geo_smoke.values(),align="center")
    plt.xticks(x_values, geo_smoke.keys())
    plt.xlabel('Interviewer geographic location')
    plt.ylabel('Fraction of smokers')
    axes = plt.gca() # get current axes
    axes.set_ylim([0,1])
    plt.savefig("plots/geo_smoke.png")
