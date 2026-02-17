class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:

        #Make list to store possible combination
        possibilities = []

        #Iterate through hours
        for i in range(12):
            #Iterate through minues
            for j in range(60):
                #Check if the number of ON bits in the hour plus ON bits in minutes equals turnedOn 
                if bin(i).count('1') + bin(j).count('1') == turnedOn:
                    #If the equal add it to possibilities
                    possibilities.append("f{i}:{j:02d}")

        return possibilities