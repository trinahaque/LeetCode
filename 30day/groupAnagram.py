# given an array of strings, group anagram together
# Time Complexity: O(M*N) --> each word in list and sorting each char in a word
# Space Complexity: O(m*n) --> hashmap and list
def groupAnagrams(strs):
    hash_map = {}
    # looping through each word: O(N)
    for each_word in strs:
        # sorting each word: O(M)
        sorted_word = ''.join(sorted(each_word))
        if sorted_word not in hash_map:
            hash_map[sorted_word] = [each_word]
        else:
            hash_map[sorted_word].append(each_word)
    # list takes O(n) space
    return list(hash_map.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(groupAnagrams(strs))