class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        
        #For every element in array sort by number of on bits and if those are same sort by number itself
        #To do this use tuple
        #Python checks first part of tuple and sees if bin(x).count("1") are same if the are checks x to see which is greater
        arr.sort(key=lambda x: (bin(x).count("1"),x))
        return arr