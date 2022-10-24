class TimeMap:

    def __init__(self):
        # Initialise a hashmap that uses
        # key : [value, timestamp]
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # check if key exists, if not create an empty list to append values
        if key not in self.store:
            self.store[key] = []
        # append values 
        self.store[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        # 1. Get the list of pairs based on keys
        values = self.store.get(key, [])
        # 2. Initialise default result value
        res = ""
        
        # 3. Since pairs are sorted by timestamp, since each append method adds value-pairs in increasing timestamp order,
        #    Use binary search
        # Note: Question requires returning value from exact timestamp, or closest exact timestamp from the left
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            # Return exact value if found
            if values[m][1] == timestamp:
                return values[m][0]
            # if middle-pointer is larger than timestamp, just update ranges
            if values[m][1] > timestamp:
                r = m - 1
            # if middle-pointer is between timestamp left pointer, its considered candidate for closest exact timestamp,
            # so update result, and update left pointer to inch closer to true timestamp value to get better result
            else: 
                l = m + 1
                res = values[m][0]
        return res
