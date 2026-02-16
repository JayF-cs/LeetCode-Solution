class Solution:
    def reverseBits(self, n: int) -> int:
        
        #Make sure n is 32 bits
        n &= 0xFFFFFFFF
        #return the reversed binary converted back to int
        return (int(f"{n:032b}"[::-1],2))
    
    def reverseBitsBetter(self, n: int) -> int:

        result = 0
        #Loop in range in 32 to ensure 32 bits
        for i in range(32):
            result = (result << 1) | (n & 1)
            n >> 1
        
        return result