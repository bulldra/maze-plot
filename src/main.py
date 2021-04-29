import numpy
import maze
import plotmaze
import settings

def updateTheta(theta, pi, history):
    eta = 0.2
    t = len(history) - 1
    [m, n] = theta.shape
    delta_theta = theta.copy()

    for sidx in range(0, m):
        state_num = len([sa for sa in history if sa['state'] == sidx])
        for aidx in range(0, n):
            if numpy.isnan(theta[sidx][aidx]):
                continue
            action_in_state_num = len([sa for sa in history if sa['state'] == sidx and sa['action'] == aidx])
            delta_theta[sidx][aidx] = (action_in_state_num + pi[sidx][aidx] * state_num) / t
    return theta + eta * delta_theta

def main():
    numpy.set_printoptions(precision=3, suppress=True)
    maze_task = maze.maze_task()
    maze_task.randomizeWall(settings.maze['maze_width'], settings.maze['maze_height'])

    plot = plotmaze.plotmaze(maze_task)
    plot.initMazePlot()
    plot.saveImage()

    theta = maze_task.convertTheta()
    pi = maze_task.convertPi(theta)
    lerning = []
    for i in range(0, 10000):
        result, history = maze_task.goalMaze(pi)
        if i == 0:
            print(f'step: {i+1}')
            print(pi)
            plot.execute(history)
        if result is True:
            lerning.append({'step': i+1, 'result': len(history) - 1})
            theta = updateTheta(theta, pi, history)
            new_pi = maze_task.convertPi(theta)

            if numpy.sum(numpy.abs(new_pi - pi)) > 10 ** -5:
                pi = new_pi
            else:
                print(f'step: {i+1}')
                print(new_pi)
                plot.execute(history)
                print(history)
                break
        else:
            lerning.append({'step': i+1, 'result': -1})

if(__name__ == '__main__'):
    main()
