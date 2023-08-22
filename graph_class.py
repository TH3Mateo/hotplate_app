from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from matplotlib import pyplot as plt
import numpy as np
import queue
class Graph(FigureCanvasKivyAgg):
    out = plt.figure()
    plt.ion()

    def __init__(self, **kwargs):
        super(Graph, self).__init__(figure=self.out, **kwargs)
        self.point_queue = queue.Queue()

    ax = out.add_subplot(111)
    out.set(facecolor=(0, 0, 0, 0))
    signal = [7, 89.6, 45. - 56.34]
    signal = np.array(signal)

    ax.plot(signal)
    ax.set_xlabel('Time(s)')

    # setting y label
    ax.set_ylabel('signal (norm)')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.grid(True, color='lightgray')
    # ax.draw()
