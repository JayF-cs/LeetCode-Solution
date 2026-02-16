class Solution:
    def reverseBits(self, n: int) -> int:
        
        #Make sure n is 32 bits
        n &= 0xFFFFFFFF
        #return the reversed binary converted back to int
        return (int(f"{n:032b}"[::-1],2))