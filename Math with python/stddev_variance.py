# variance and standard deviation
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
if __name__ == '__main__':
 donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
 variance = calc_variance(donations)
 print("variance :",variance)
 std = variance**0.5
 print("std deviation :",std)
