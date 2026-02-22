class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        
        #Make helper function to check if number of set bits is prime
        #Use optimized trial division
        def is_prime(n:int) -> bool:
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            
            i = 5

            while i*i < n:

                if n % i == 0 or n % (i+2) == 0:
                    return False
                i += 6

            return True

        #loop through everything including bounds and check if is prime
        count = 0
        for i in range(left,right+1):
            if is_prime(bin(i).count('1')):
                count+=1

        return count