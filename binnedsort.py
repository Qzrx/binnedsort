import random
import timeit

# Our bad sorting algorithm
def sucksort(numbers):
  i = 0
  # Returns the index of the minimal element in a list
  def mindex(tail):
    idx = 0
    smallest = tail[0]
    i = 0
    while i < len(tail):
      if tail[i] < smallest:
        idx = i
        smallest = tail[i]
      i += 1
    return idx
  # Now go through, grab the smallest element, place it at the head. Repeat.
  while i < len(numbers):
    # Get idx of smallest.
    min_idx = mindex(numbers[i:])
    # Pop it, place in front
    numbers.insert(0,numbers.pop(i+min_idx))
    i += 1
  return numbers

# Generates n random numbers in {-100,100}
def random_number_list(n):
  x = []
  i = 0
  while i < n:
    x.append(random.randrange(-100,100))
    i += 1
  return x

# First thing we need is a function to find the median of a list
#
# vector: a list to find the sample median of
# n     : the number of elements from the head of vector to sample to calculate the median
def sample_median(vector, n):
  # So...we need to sort our vector to find the median, as far as I can tell. Looks like
  # we're baking a pie from scratch.
  l = len(vector)
  if n <= l:
    x = vector[:n]
  else:
    x = vector[:]
    n = l
  # Yes, we're going to use sucksort() here. For small N, who cares?
  sucksort(x)
  if n%2 == 1:
    median = x[(n+1)/2]
  else:
    median = (x[(n/2)-1] + x[(n/2)])/2
  return median

def binnedsort(vector):
  if len(vector) == 1:
    return vector
  if len(vector) == 2:
    if vector[0] <= vector[1]:
      return vector
    else:
      return [vector[1], vector[0]]
  else:
    m = sample_median(vector, 20)
    L = []
    R = []
    for x in vector:
      if x <= m:
        L.append(x)
      else:
        R.append(x)
  if R == []:
    return L
  else:
    return binnedsort(L) + binnedsort(R)

def test(n):
        rn = random_number_list(n)
        binnedsort(rn)

if __name__ == '__main__':
    import timeit
    print "Sorting random list of size 1       : ", timeit.timeit("test(1)", setup="from __main__ import test", number=1),"s"
    print "Sorting random list of size 10      : ", timeit.timeit("test(10)", setup="from __main__ import test", number=1),"s"
    print "Sorting random list of size 100     : ", timeit.timeit("test(100)", setup="from __main__ import test", number=1),"s"
    print "Sorting random list of size 1000    : ", timeit.timeit("test(1000)", setup="from __main__ import test", number=1),"s"
    print "Sorting random list of size 10000   : ", timeit.timeit("test(10000)", setup="from __main__ import test", number=1),"s"
    print "Sorting random list of size 100000  : ", timeit.timeit("test(100000)", setup="from __main__ import test", number=1),"s"
    print "Sorting random list of size 1000000 : ", timeit.timeit("test(1000000)", setup="from __main__ import test", number=1),"s"
    print "Sorting random list of size 10000000: ", timeit.timeit("test(10000000)", setup="from __main__ import test", number=1),"s"
    print "Finished!"
