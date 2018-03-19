import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
''''''
fig = plt.figure()
ax1 = plt.axes(xlim=(0,10), ylim=(0,-10))


def animate(i):
    pulldata = open("C:\\Users\\anshul\\jupyter\\sample.txt", "r").read()
    lines = pulldata.split('\n')
    dates = []
    for l in range(len(lines) - 1):
        dates.append((lines[l].split(' '))[1])

    dates1 = np.unique(dates)
    #print(dates1)
    xar = []
    yar = []
    x = 0
    par = []
    nar = []
    near = []
    for d1 in range(len(dates1)):
        p = 0
        n = 0
        ne = 0
        xar.append(dates1[d1])
        #print (str)
        for d2 in range(len(dates)):

            if dates1[d1] == dates[d2]:
                if 'Positive' in lines[d2]:
                    p += 1
                elif 'Negative' in lines[d2]:
                    n += 1
                else:
                    ne += 1
        par.append(np.mean(p))
        nar.append(np.mean(n))
        near.append(np.mean(ne))
    ax1.clear()
    pos = ax1.plot(xar, par, 'o-', color='r', label='Positive')
    neg = ax1.plot(xar, nar, 'o-', color='g', label='Negative')
    neu = ax1.plot(xar, near, 'o-', color='b', label='Neutral')
    ax1.legend(loc='upper right')
    plt.xlabel("Days")
    plt.ylabel("No. of tweets in a day")
    plt.xticks(rotation=60)


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
