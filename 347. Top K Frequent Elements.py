class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # make a hashmap to quantify count of each element
        freq = [[] for i in range(len(nums)+1)] # makes [[],[],[],..] based on  length of input array

        for n in nums: # creates a hashmap of key(element) and value(frequency or quantity of element)
                count[n] = 1 + count.get(n, 0) # with default value 0, increments the value associated with the key in hashmap
        for n,c in count.items(): # count.items() is enumerator for all K-V pair in hashmap
                freq[c].append(n) # for each possible frequency c, adds the element that occurs that many time to the nested array in position c

        res = [] # creates a results array
        for i in range(len(freq)-1, 0, -1): # creates decreasing number from len-1 to 0
                for n in freq[i]:
                    res.append(n) # keeps appending element to array until len == k
                if len(res) == k:
                    return res
