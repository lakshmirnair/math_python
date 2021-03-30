#creating a grouped frequency table
def create_classes(num, n):
  low = min(num)
  high = max(num)
  width = (high - low)/n
  clas = []
  a = low
  b = low + width
  while a < (high-width):
     clas.append((a, b))
     a = b
     b = a + width
  clas.append((a, high+1))
  return clas
def frequency(num,clas):
    f=[]
    for i in clas:
        ct=0;
        for j in num:
            if(j<=i[1] and j>=i[0]):
                a=j
                ct=ct+1
        f.append(ct)
    return f;
if __name__=='__main__':
    li=[7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
    a=[]
    f=[]
    a=create_classes(li,4)
    f=frequency(li,a)
    print("class"+"   "+"frequency")
    for i,j in zip(a,f):
        print(str(i)+"  "+str(j))
