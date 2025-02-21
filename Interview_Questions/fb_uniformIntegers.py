def getUniformIntegerCountInInterval(A: int, B: int) -> int:
  # Stores the result
  countUniformDigits = 0
  # Calculation depends on the delta between digit lengths of A & B
  digitLength_A, digitLength_B = len(str(A)), len(str(B))
  diff_digit_length = digitLength_B - digitLength_A - 1
  # A & B are at least 1 digit length different
  if diff_digit_length >= 0:
    countUniformDigits += determineRemainingUniformDigitsForALength(A)
    countUniformDigits += diff_digit_length * 9
    countUniformDigits += determineLastUniformDigitsLeadingToB(B)
  # A & B have the same digit length
  else:
    countUniformDigits += determineUniformDigitsABSameLength(A,B)

  return countUniformDigits

def isUniform(integer: int) -> bool:
  # Work with string is an efficient way to determine int `uniformity`
  integerStr = str(integer)
  # Safety check
  if len(integerStr) < 1:
    return False
  # Evaluate `uniformity`, if all digits are the same
  firstDigit = integerStr[0]
  for digit in integerStr:
    if digit != firstDigit:
      return False
  return True

# Finds closest uniform integer depending on input integer's first digit
def determineNextUniformDigit(integerStr: str) -> str:
  return "".join([f'{integerStr[0]}' for x in integerStr])

# Find uniform integers above A in the same digit length
# i.e. A = 56; then 66, 77, 88, 99 - so 4
def determineRemainingUniformDigitsForALength(A: int) -> int:
  nextUniformDigit = determineNextUniformDigit(str(A))
  firstDigit = int(nextUniformDigit[0])
  if A <= int(nextUniformDigit):
    return 9 - firstDigit + 1
  else:
    return 9 - firstDigit
  
# Find uniform integers below B in the same digit length
# i.e. B = 556; then 555, 444, 333, 222, 111 - so 5
def determineLastUniformDigitsLeadingToB(B: int) -> int:
  nextUniformDigit = determineNextUniformDigit(str(B))
  if B < int(nextUniformDigit):
    return int(nextUniformDigit[0]) - 1
  else:
    return int(nextUniformDigit[0])
  

def determineUniformDigitsABSameLength(A: int, B: int) -> int:
  nextUniformDigit_A = determineNextUniformDigit(str(A))
  nextUniformDigit_B = determineNextUniformDigit(str(B))
  if int(nextUniformDigit_A) < int(nextUniformDigit_B):
    count = int(nextUniformDigit_B[0]) - int(nextUniformDigit_A[0]) + 1
    count -= 1 if A > int(nextUniformDigit_A) else 0
    count -= 1 if B < int(nextUniformDigit_B) else 0
    return count
  elif int(nextUniformDigit_A) == int(nextUniformDigit_B):
    return 1 if isUniform(A) else 0
  else:
    return 0
