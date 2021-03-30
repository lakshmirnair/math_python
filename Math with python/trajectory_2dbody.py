# x=ucosθ t
#y=usinθ t-1/2(g t^2)
#Drwawing the trajectory of 2d motion
#comparing the trajectory with different initial values
from matplotlib import pyplot as plt
import math
def graph(x,y):
    plt.plot(x,y)
    plt.xlabel('x coordinate')
    plt.ylabel('y cordinate')
    plt.title('projectile motion of a ball')

def frange(s,f,i):
    n=[]
    while(s<f):
        n.append(s)
        s=s+i
    return n
def trajectory(u,theta):
    th=math.radians(theta)
    g=9.8
    t_flight=2*u*math.sin(theta)/g
    inte=frange(0,t_flight,0.0001)
    x=[]
    y=[]
    for t in inte:
        x.append(u*math.cos(th)*t)
        y.append(u*math.sin(theta)*t-0.5*g*t*t)
    graph(x,y)
if __name__=='__main__':
    li=[20,40,60]
    theta=45
    for i in li:
        trajectory(i,theta)
    plt.legend(['20','40','60'])
    plt.show()
