from typing import List
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    
    # stores word sorted in alphabetical order as key, with index to lists of lists as value
    anagrams_dict = {}

    # stores list of lists, anagrams, to return
    anagrams = []

    # indexing list of list as new anagrams are discovered
    count = 0

    # every string
    for i in strs:

        # sort so that it will match anagram
        sorted_word = sorted(i)

        # put back together in one string
        sorted_word = ''.join(sorted_word)

        # anagram already discovered, append word to list
        if sorted_word in anagrams_dict:
            anagrams[anagrams_dict[sorted_word]].append(i)

        # new anagram, append new list with word and update dictionary with key, index
        else:
            anagrams.append([i])
            anagrams_dict[sorted_word] = count
            count += 1

    return anagrams

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))