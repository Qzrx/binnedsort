def binsort2(input):
  if not input: return []
  else: 
    pivot = input[0]
    return binsort2([n for n in input[1:] if n <= pivot]) + [input[0]] + binsort2([n for n in input[1:] if n > pivot])
