import matplotlib.pyplot as plt
import matplotlib.animation as animation

''''''
fig = plt.figure()
ax1 = plt.axes(xlim=(0,10), ylim=(0,-10))


def animate(i):
    pulldata = open("C:\\Users\\anshul\\jupyter\\sample.txt", "r").read()
    lines = pulldata.split('\n')
    xar = []
    #yar=[]

    par = []
    nar = []
    near = []
    p = 0
    n = 0
    ne = 0

    x = 0
    y=0
    for l in lines:
        x += 1
        if 'Positive' in l:
            p += 1
        elif 'Negative' in l:
            n +=1
        else:
            ne += 1

        xar.append(x)
        #yar.append(y)

        par.append(p)
        nar.append(n)
        near.append(ne)


    labels=[('positive',(p/x)),('negative',(n/x)),('neutral',(ne/x))]
    sizes=[(p/x), (n/x), (ne/x)]
    colors=['red','green','blue']
    ax1.clear()
    ax1.pie(sizes, labels=labels, colors=colors)
    circle=plt.Circle(xy=(0,0), radius=0.75, facecolor='white')
    plt.gca().add_artist(circle)

    ax1.plot(xar, nar, 'b')
    ax1.plot(xar, near, 'g')


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
