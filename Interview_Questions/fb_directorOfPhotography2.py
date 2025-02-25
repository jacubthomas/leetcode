from typing import List
def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  # Result stored here
  count = 0

  # Calculate the Prefix-Sums - Sums of P or B leading up to a given index
  photographerPrefix = [0] * (N+1)
  backdropPrefix = [0] * (N+1)
  for i in range(N):
    photographerPrefix[i + 1] = photographerPrefix[i] + (1 if C[i] == 'P' else 0)
    backdropPrefix[i + 1] = backdropPrefix[i] + (1 if C[i] == 'B' else 0)
  
  # Consider the string entire, creating windows for counting as we find actors
  for i in range(0,N):
    if C[i] == "A":
      left_P = countRange(photographerPrefix, max(0, i - Y), max(0, i - X + 1))
      left_B = countRange(backdropPrefix, max(0, i - Y), max(0, i - X + 1))
      right_P = countRange(photographerPrefix, min(N, i + X), min(N, i + Y + 1))
      right_B = countRange(backdropPrefix, min(N, i + X), min(N, i + Y + 1))

      count += left_P * right_B + left_B * right_P

  return count

def countRange(prefixSum: List[int], leftEdge, rightEdge):
  if leftEdge >= rightEdge:
    return 0
  return prefixSum[rightEdge] - prefixSum[leftEdge]
