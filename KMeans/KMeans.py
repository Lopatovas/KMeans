import numpy
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
from collections import Counter

import utils
import graphics
import const
import config

def clusterData(data, x, y, k):
    kMeans = KMeans(n_clusters=k).fit_predict(data[[x, y]])
    print(x,y,Counter(kMeans))
    graphics.plotScatter(data, x, y, '{}/{} data after clustering with {} clusters'.format(x, y, k), kMeans=kMeans)
    silhouetteValidate(data, kMeans, k)

def silhouetteValidate(data, kMeans, k):
    silhouetteAvg = silhouette_score(data, kMeans)
    silhouetteValues = silhouette_samples(data, kMeans)
    graphics.plotSilhouette(silhouetteValues, silhouetteAvg, kMeans, k, len(data))
    

def clusterDataPairs(data, kMin, kMax):
    for pair in const.DATA_PAIRS:
        graphics.plotScatter(data, pair[0], pair[1], '{}/{} data before clustering'.format(pair[0], pair[1]))
        for k in range(kMin, kMax+1):
            clusterData(data, pair[0], pair[1], k)

def driver():
    data = utils.readData()
    clusterDataPairs(data, config.MIN_CLUSTERS, config.MAX_CLUSTERS)

driver()