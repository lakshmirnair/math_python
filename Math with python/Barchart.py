import matplotlib.pyplot as plt
def barchart(data, labels):
    num_bars=len(data)
    pos=range(1,num_bars+1)
    plt.barh(pos,data,align="center")
    plt.yticks(pos,labels)
    plt.xlabel('steps')
    plt.ylabel('day')
    plt.title('numbers of steps walked')
    plt.grid()
    plt.show()
if __name__ == '__main__':
# data
   steps = [6534, 7000, 8900, 10786, 3467, 11045, 5095]
   labels = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
   barchart(steps, labels)
