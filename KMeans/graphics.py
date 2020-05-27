import matplotlib.pyplot as plt
import numpy
from matplotlib import cm

def plotScatter(data, x, y, title, **kwargs):
    kMeans = kwargs.get('kMeans', [])
    if len(kMeans) > 0:
        viridis = cm.get_cmap('copper', 8)
        plt.scatter(data[x], data[y], c=kMeans, cmap=viridis)
    else:
        plt.scatter(data[x], data[y])
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(title)
    plt.show()

def plotSilhouette(silhouetteValues, silhouetteAvg, kMeans, k, dataCount, xLabel, yLabel):
    _, ax = plt.subplots()
    y_lower = 10
    ax.set_xlim([-1, 1])
    ax.set_ylim([0, dataCount + (k + 1) * 10])
    for i in range(k):
        ithClusterSilhouetteValues = \
            silhouetteValues[kMeans == i]
        ithClusterSilhouetteValues.sort()
        size_cluster_i = ithClusterSilhouetteValues.shape[0]
        y_upper = y_lower + size_cluster_i
        ax.fill_betweenx(numpy.arange(y_lower, y_upper), 0, ithClusterSilhouetteValues)
        ax.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))
        y_lower = y_upper + 10

    ax.set_title('Silhouette plot for {}/{} with {} clusters'.format(xLabel, yLabel, k))
    ax.set_xlabel('Silhouette coefficient values')
    ax.set_ylabel('Cluster number')
    ax.axvline(x=silhouetteAvg, color="red", linestyle="--")

    ax.set_yticks([])
    ax.set_xticks([-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1])
    plt.show()
    print('Average Silhouette value for {}/{} is {}'.format(xLabel, yLabel, silhouetteAvg))