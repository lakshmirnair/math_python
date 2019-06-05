# Correlation between two list of data
def mean(num):
    s=sum(num)
    n=len(num)
    m=s/n
    return m
def find_diff(num):
    me=mean(num)
    dif=[]
    for i in num:
        dif.append(i-me)
    return dif
def calc_variance(numbers):
   diff = find_diff(numbers)
   squared_diff = []
   for d in diff:
      squared_diff.append(d**2)
   sum_squared_diff = sum(squared_diff)
   variance = sum_squared_diff/len(numbers)
   return variance
def calc_coreelation(x,y,a,b):
    n=len(x)
    p=[]
    for xi,yi in zip(x,y):
        p.append(xi*yi)
    sum_p=sum(p)
    sum_x=sum(x)
    sum_y=sum(y)
    numt=sum_p/n -(sum_x*sum_y /(n*n))
    dent=a*b
    core=numt/dent
    return core

if __name__ == '__main__':
 x = [1,2,3]
 y = [2,4,6]
 v1 = calc_variance(x)
 s1 = v1**0.5
 v2 = calc_variance(y)
 s2 = v2 ** 0.5
 core=calc_coreelation(x, y, s1,s2)
 print("correlation :",core)
