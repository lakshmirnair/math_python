import matplotlib.pyplot as plt
def graph(x,y):
    plt.plot(x,y,marker='o')
    plt.xlabel('distance in meter')
    plt.ylabel('force in Newton')
    plt.title('Gravitational force Vs distance')
    plt.show()
def force():
    r=range(100,1001,50)
    f=[]
    G=6.67*(10**-11)
    m1,m2=0.5,1.5
    for i in r:
        fo=G*m1*m2/(i**2)
        f.append(fo)
    graph(r,f)
if __name__=='__main__':
   force()
