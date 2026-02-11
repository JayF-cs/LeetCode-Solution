
class Solution:
    def longestBalanced(self, nums: list[int]) -> int:
        #Make var to hold max value
        maxSize = 0
        #Get length of nums
        l = len(nums)
        #Iterate over nums
        for i in range(l):
            #Make sets for even and odd number to store unique numbers
            even = set()
            odd = set()
            #Iterate starting at i going to end
            for j in range(i,l):
                #Check if it is even or odd and add to proper array
                if nums[j] % 2:
                    odd.add(nums[j])
                else:
                    even.add(nums[j])
                #Check if lengths of the two sets are even and if they are then you have a subarray with same number of unique odd and even elements
                if len(even) == len(odd):
                    #Set maxSize to largest between subarray length and max size
                    maxSize = max(maxSize, j - i + 1)

        return maxSize