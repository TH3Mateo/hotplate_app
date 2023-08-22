import numpy as np

import connection_module
import matplotlib
from matplotlib import pyplot as plt
import numpy
# matplotlib.use('qtagg')
matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')
# noinspection PyUnresolvedReferences
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvas, NavigationToolbar2Kivy, FigureCanvasKivyAgg
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import (NumericProperty, StringProperty, ReferenceListProperty, ObjectProperty)
from kivy.config import Config
from kivy.clock import Clock
import connection_module
from kivy.uix.label import Label
from kivy.core.window import Window

Window.size = (1000,800)
Window.clearcolor = (61 / 255, 43 / 255, 52 / 255, 1)
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '200')
Builder.load_file("visuals.kv")
glob_counter = 0

class Graph(FigureCanvasKivyAgg):
    out = plt.figure()
    plt.ion()

    def __init__(self, **kwargs):
        super(Graph, self).__init__(figure=self.out, **kwargs)

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


class Confirm(Button):
    holder = 0


class View(FloatLayout):
    connection = connection_module.start()

    def on_text(self):
        Confirm.holder = self.ids.target.text
        print(Confirm.holder)

    def press(self):
        self.ids.set_t.text = str(self.ids.butn.holder)
        # self.connection.write(str(self.ids.butn.holder).encode('utf-8'))

    def update(self, *args):

        try:
            self.ids.temp.text = connection_module.filter_temp(self.connection.readline().decode('utf-8'))
        except:
            pass

    def refresh(self, *args):
        print("button")

        self.ids.grph.ax.clear()
        self.ids.grph.ax.set(facecolor=(0, 1, 0, 1))
        # self.ids.grph.ax.show()
        #
        self.ids.grph.ax.plot(self.ids.grph.signal)
        self.ids.grph.draw()
        self.ids.grph.flush_events()



class GUIapp(App):
    def on_start(self):
        Clock.schedule_interval(self.root.update, 0.5)

    def build(self):
        return View()


if __name__ == '__main__':
    GUIapp().run()
