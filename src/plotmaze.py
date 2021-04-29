import numpy
import datetime
import matplotlib.pyplot as pyplot
import matplotlib.animation as animation

class plotmaze:
    def __init__(self, maze):
        self.maze = maze

    def execute(self, history):
        figure = self.initMazePlot()
        self.history = history
        self.anim = animation.FuncAnimation(figure, self.animate, frames=len(history), interval=150, repeat=False)
        self.saveAnimation()

    def saveImage(self):
        figure = self.initMazePlot()
        now = datetime.datetime.now()
        figure.savefig(f'plot_{now:%Y%m%d_%H%M%S}.png')

    def saveAnimation(self):
        now = datetime.datetime.now()
        self.anim.save(f'plot_{now:%Y%m%d_%H%M%S}.gif', writer='imagemagick')

    def initMazePlot(self):
        mazewidth = self.maze.width()
        mazeheight = self.maze.height()
        figure = pyplot.figure(figsize=(5, 5))
        axes = figure.add_subplot(111)
        axes.text(0.5, mazeheight - 0.7, 'START', ha='center')
        axes.text(mazewidth-0.5, 0.3, 'GOAL', ha='center')

        for y in range(0, mazeheight):
            for x in range(0, mazewidth):
                px = x
                py = mazeheight - y
                axes.text(px + 0.5, py - 0.5, f'S{x + y * mazewidth}', size=7, ha='center')
                if self.maze.getWall(x, y) in [1, 3]:
                    axes.plot([px + 1, px + 1], [py, py - 1], color='blue', linewidth=2)
                if self.maze.getWall(x, y) in [2, 3]:
                    axes.plot([px, px + 1], [py - 1, py - 1], color='red', linewidth=2)

        axes.set_xlim(0, mazewidth)
        axes.set_ylim(0, mazeheight)
        axes.tick_params(axis='both', which='both', bottom='off', top='off',
                labelbottom='off', right='off', left='off', labelleft='off')

        self.mark, = axes.plot([0.5], [mazewidth -0.5], marker="o", color='g', markersize=20)
        self.counter = axes.text(mazewidth -0.5, 0.1, '0', ha='center')

        return figure

    def animate(self, i):
        mazewitdh = self.maze.width()
        mazeheight = self.maze.height()
        state = self.history[i]['state']

        x = (state % mazewitdh) + 0.5
        y = mazeheight - 0.5 - int(state / mazewitdh)

        self.mark.set_data(x, y)
        self.counter.set_text(i)
