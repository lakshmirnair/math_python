def read_data(file):
    s=0
    with open(file) as f:
        for line in f:
            s=s+float(s)
    print("sum :", s)
if __name__=="__main__":
    read_data('data1.txt')
