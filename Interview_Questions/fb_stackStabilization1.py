from typing import List

def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
  # A stable stack will have strictly increasing radius from top -> bottom
  # But we can only decrease (deflate), so let's work greedily from bottom -> top
  R.reverse()
  # Track number of discs deflated for return result
  count = 0
  # Consider all discs above the bottom most
  for i in range(1, len(R)):
    # Disc above has larger radius, needs deflating
    if R[i] >= R[i-1]:
      R[i] = R[i-1] - 1
      count += 1
    # We can no longer deflate a disc that is currently making the stack unstable
    if R[i] < 1:
      return -1
  return count
