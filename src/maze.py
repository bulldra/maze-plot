import numpy

class maze_task:
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def setWall(self,wall):
        self.wall = wall

    def randomizeWall(self, x, y):
        isOk = False
        for i in range(1000):
            self.wall = numpy.random.randint(0, 3, (y, x))
            pi = self.convertPi(self.convertTheta())
            result, history = self.goalMaze(pi)
            if result is True:
                isOk = True
                break
        if isOk is False:
            raise ValueError("error!")

    def height(self):
        return len(self.wall)

    def width(self):
        return len(self.wall[0])

    def getWall(self, x, y):
        return self.wall[y][x]

    def convertTheta(self):
        m = self.height()
        n = self.width()

        theta = numpy.zeros([int(m * n), 4])
        theta[:][:] = 1

        for i in range(m * n):
            if int(i / n) == 0:
                theta[i][self.UP] = numpy.nan
            if int(i % n) == 0:
                theta[i][self.LEFT] = numpy.nan
            if int(i / n) == m - 1:
                theta[i][self.DOWN] = numpy.nan
            if int(i % n) == n - 1:
                theta[i][self.RIGHT] = numpy.nan
            if self.wall[int(i / n)][i % n] in [1, 3]:
                theta[i][self.RIGHT] = numpy.nan
            if self.wall[int(i / n)][i % n] in [2, 3]:
                theta[i][self.DOWN] = numpy.nan
            if i / n >= 1 and self.wall[int(i / n) - 1][i % n] in [2, 3]:
                theta[i][self.UP] = numpy.nan
            if i % n >= 1 and self.wall[int(i / n)][i % n - 1] in [1, 3]:
                theta[i][self.LEFT] = numpy.nan

        return theta

    def convertPi(self, theta):
        beta = 1.0
        [m, n] = theta.shape
        pi = numpy.zeros((m, n))
        exp_theta = numpy.exp(beta * theta)
        for i in range(0, m):
            pi[i][:] = exp_theta[i][:] / numpy.nansum(exp_theta[i][:])
        return numpy.nan_to_num(pi)

    def goalMaze(self, pi):
        state = 0
        state_history = []

        for i in range(100):
            (action, next_state) = self.next(pi, state)
            state_history.append({'state': state, 'action': action})
            if next_state == pi.shape[0] - 1:
                state = next_state
                state_history.append({'state': state, 'action': numpy.nan, 'step': i})
                return True, state_history
            else:
                state = next_state
        return False, state_history

    def next(self, pi, state):
        width = self.width()
        next_state_offset = (-width, 1, width, -1)
        action = numpy.random.choice(a=list(range(0, 4)), p=pi[state, :])
        return [action, state + next_state_offset[action]]
