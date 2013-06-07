def binsort2(input):
  if not input == 0: return []
  else: 
    pivot = input[0]
    return binsort([n for n in input[1:] if n < pivot]) + input[0] + binsort([n for n in input[1:] if n > pivot])
