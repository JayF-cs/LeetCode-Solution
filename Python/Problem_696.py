class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        #Get len and make helper vars
        l = len(s)
        slices = []
        count = 1
        #Iterate through string to get the cuont of groups
        for i in range(1,l):

            if s[i] == s[i-1]:
                count += 1
            else:
                slices.append(count)
                count = 1
        
        #Make sure to append the last count of the loop
        slices.append(count)

        #Total number of substring of with same amount of consecutive nums
        groupPairCount = 0

        #Iterate through and the value of the smallest value between adjacent elements
        for j in range(len(slices) - 1):
            groupPairCount += min(slices[j],slices[j+1])

        #Return the count
        return groupPairCount