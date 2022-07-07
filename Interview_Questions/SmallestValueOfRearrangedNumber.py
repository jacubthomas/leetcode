# You are given an integer num. Rearrange the digits of num such that its value 
# is minimized and it does not contain any leading zeros. Return the rearranged
# number with minimal value. Note that the sign of the number does not change 
# after rearranging the digits.

# Example 1:
# Input: num = 310
# Output: 103
# Explanation: The possible arrangements for the digits of 310 are 013, 031, 103, 130, 301, 310. 
# The arrangement with the smallest value that does not contain any leading zeros is 103.

# Example 2:
# Input: num = -7605
# Output: -7650
# Explanation: Some possible arrangements for the digits of -7605 are -7650, -6705, -5076, -0567.
# The arrangement with the smallest value that does not contain any leading zeros is -7650.
 

# Constraints:
# -1015 <= num <= 1015

def smallestNumber(num: int) -> int:
    if num == 0:
        return num

    # if neg, want largest number; if pos, smallest w/ no leading zeroes
    isNeg = num/abs(num)
    print("isNeg: ", isNeg)
    num = abs(num)
    num_list = list(str(num))
    print(num_list)
    
    zero_count = 0

    if isNeg < 0:
        num_list.sort(reverse = True)
        num = int(''.join(num_list)) * (-1)
        print(num)
        return num
    else:
        num_list.sort()
        for i in num_list:
            # print(i)
            if i == '0':
                zero_count +=  1
            else:
                break
        
        num = str(num_list[zero_count])
        # print(num.ljust(zero_count+1, "0"))

        remain = num_list[zero_count+1:]
        num = list(num.ljust(zero_count+1, "0"))
        # print("num: ", num)
        # print("remain: ", remain)
        num_list = list(num) + remain
        # print("num+remain: ", num_list)
        # print("count: ", zero_count)
        num = int(''.join(num_list))
        print(num)
        return num


smallestNumber(500004)















        # idea sort num as string, then move all leading zeroes in one or to end


        # # Preserves value of num
        # temp_num = num

        # # Counts length of digits in num
        # digits = len(str(num))

        # # Check if num is 0
        # if num  == 0:
        #     return temp

        # # Find smallest value in num that is not 0
        
        # while()
        # # Find 2nd smallest value in num
        #     # Repeat