
def checkInclusion(s1: str, s2: str) -> bool:
    # Impossible to have permutation if s1 > s2
    if len(s1) > len(s2): return False

    # Create Hashmaps to quantify count
    s1Map = {}
    s2Map = {}

    # Create hashmap for s1, while creating first sliding window in s2, based on length of s1
    for i in range(len(s1)):
        s1Map[s1[i]] = 1 + s1Map.get(s1[i], 0)
        s2Map[s2[i]] = 1 + s2Map.get(s2[i], 0)
    
    # If first window is a hit, return True
    if s1Map == s2Map:
        return True
    
    # Create pointers 
    # right pointer is set to 1 position after first window for easier coding
    l, r = 0, len(s1)

    # Sliding window
    # r-pointer adds values, l-pointer removes values
    for r in range(len(s1), len(s2)):
        # Adds new char from new position of r-pointer
        s2Map[s2[r]] = 1 + s2Map.get(s2[r], 0)

        # Removes char on l-pointer position
        s2Map[s2[l]] -= 1
        
        # l-pointer removes empty keys
        if s2Map[s2[l]] == 0:
            del s2Map[s2[l]]
        # Shift l-pointer only after removing empty keys from previous position, and removing values
        l += 1

        # Checks if Hashmaps match
        if s1Map == s2Map:
            return True
    return False

# Testcase
if __name__ == "__main__":
    u = "ab"
    s = "eidbaooo"
    answer = checkInclusion(u,s)
    print(answer)