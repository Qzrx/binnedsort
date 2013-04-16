# Calculates a median from the first n items of a list
# vector: a list to find the sample median of
# n     : the number of elements from the head of vector to sample to calculate the median
def sample_median(vector, n):
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

# Sorts a vector using binnedsort. I'd call it binsort, but that's a real thing, and I suspect
# that it isn't remotely this bad.
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
