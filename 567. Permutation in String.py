
def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2): return False

    s1Map = {}
    s2Map = {}

    for c in s1:
        s1Map[c] = 1 + s1Map.get(c, 0)
    
    l,r,c = 0,len(s1) - 1, 0

    while r < len(s2):
        c = l
        while l < r + 1:
            s2Map[s2[l]] = 1 + s2Map.get(s2[l], 0)
            l += 1
        if s2Map == s1Map:
            return True
        else:
            l = c 
            l += 1
            r += 1
            s2Map = {}
    return False

if __name__ == "__main__":
    u = "ab"
    s = "eidbaooo"
    answer = checkInclusion(u,s)
    print(answer)