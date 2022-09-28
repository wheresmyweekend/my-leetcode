class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for word in strs:
            charCount = [0] * 26 # Creates a list of 26 zeros to count alphabets in word
            for char in word:
                charCount[ord(char) - ord("a")] += 1
            ans[tuple(charCount)].append(word) # Appends word to hashmap key of same alphabet signature
        return ans.values() 