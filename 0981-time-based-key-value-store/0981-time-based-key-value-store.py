class TimeMap:

    def __init__(self):
        # Hashmap where key=string, value= [list of [value, timestamp]]
        self.store = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If the key is not in the dictionary already initialize a list with that key
        if key not in self.store:
            self.store[key] = []
        # If it does exist append the [val,time] pair to the list associated with key
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        # List of pairs asscoiated with key [[val, time]...]
        val_list = self.store[key]

        lo = 0
        hi = len(val_list) - 1
        res = ""

        while lo <= hi:
            mid = (lo + hi) // 2
            if val_list[mid][1] <= timestamp:
                res = val_list[mid][0]
                lo = mid + 1
            else:
                hi = mid - 1
        
        return res

            
                


        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)