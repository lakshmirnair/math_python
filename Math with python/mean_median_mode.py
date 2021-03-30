from collections import Counter
def mean(n):
    s = sum(n)
    N = len(n)
    mean = s / N
    return mean
def median(numbers):
  N = len(numbers)
  numbers.sort()
  if N % 2 == 0:
    m1 = N/2
    m2 = (N/2) + 1
    m1 = int(m1) - 1
    m2 = int(m2) - 1
    median = (numbers[m1] + numbers[m2])/2
  else:
     m = (N)/2
     m = int(m)

     median = numbers[m]
  return median
def mode(n):
  c = Counter(n)
  numbers_freq = c.most_common()
  max_count = numbers_freq[0][1]
  modes = []
  for num in numbers_freq:
    if num[1] == max_count:
      modes.append(num[0])
  return modes
if __name__=='__main__':
    d = [4, 2, 1, 3, 4]
    print("mean")
    print(mean(d))
    print("median")
    print(median(d))
    print("mode")
    print(mode(d))

