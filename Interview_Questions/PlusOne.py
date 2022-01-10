from typing import List
import math


def plusOne(digits: List[int]) -> List[int]:
    i = len(digits)-1
    carry = 1
    while i >= 0:
        digits[i] += carry
        carry = math.floor(digits[i] / 10)
        digits[i] %= 10
        i -= 1
    if carry > 0:
        l = [carry]
        digits = l + digits
    return digits


l = [1, 2, 3]
print(plusOne(l))

l = [9, 9, 9]
print(plusOne(l))

l = [9]
print(plusOne(l))
