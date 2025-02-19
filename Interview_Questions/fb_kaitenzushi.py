from typing import List

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    # Map all unique dishes to `uneaten` value
    quickDishEatenLookup = dict.fromkeys(D, -1)
    # Count all dishes eaten throughout
    count = 0
    # Consider all dishes in order they appear on kaiten-belt
    for i in range(0, len(D)):
        # Dish has never been eaten, do so now
        if quickDishEatenLookup[D[i]] == -1:
            # Update when we last ate dish
            quickDishEatenLookup[D[i]] = count
            # Update total dishes consumed
            count += 1
        # Dish has not been eaten in the last k-consumed dishes
        # (count dishes eaten) - (last time we ate this dish) > K-threshold for eating dish again
        elif count - quickDishEatenLookup[D[i]] > K:
            # Update when we last ate dish
            quickDishEatenLookup[D[i]] = count
            # Update total dishes consumed
            count += 1
        
    return count

print(getMaximumEatenDishCount(N = 6, D = [1, 2, 3, 3, 2, 1], K = 1))
print(getMaximumEatenDishCount(N = 6, D = [1, 2, 3, 3, 2, 1], K = 2))
print(getMaximumEatenDishCount(N = 7, D = [1, 2, 1, 2, 1, 2, 1], K = 2))
