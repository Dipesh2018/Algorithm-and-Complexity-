def binarySearch(Values, target ) :
# Start with the entire sequence of elements.
  low = 0
  high = len(Values) - 1
# Repeatedly subdivide the sequence in half until the target is found.
  while low <= high :
#Find the midpoint of the sequence.
   mid = (high + low) // 2
# Does the midpoint contain the target?
  if Values[mid] == target :
   return True
# Or does the target precede the midpoint?
  elif target < Values[mid] :
   high = mid - 1
# Or does it follow the midpoint?
  else :
   low = mid + 1
# If the sequence cannot be subdivided further, we're done.
  return False
