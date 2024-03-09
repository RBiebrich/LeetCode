#CHALLENGE:
#===================================================================================
# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's
# triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it
# as shown:

#         [1]
#       [1] [1]
#     [1] [2] [1]
#   [1] [3] [3] [1]
# [1] [4] [6] [4] [1]

#===================================================================================

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        out = [1]

        for times in range(rowIndex):
            newout = [1]
            for i in range(len(out)):
                if i == len(out)-1:
                    newout += [1]
                else:
                    newout.append(out[i]+out[i+1])
            out = newout
        return out
