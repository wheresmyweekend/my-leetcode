class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        noOfRows, noOfCols = len(matrix), len(matrix[0])

        firstRowPointer, lastRowPointer = 0, noOfRows - 1
        while firstRowPointer <= lastRowPointer:
            middleRowPointer = (firstRowPointer + lastRowPointer) // 2
            if target > matrix[middleRowPointer][-1]:
                firstRowPointer = middleRowPointer + 1
            elif target < matrix[middleRowPointer][0]:
                lastRowPointer = middleRowPointer - 1
            else:
                break
        
        if not firstRowPointer <= lastRowPointer: # also 'if firstRowPointer > lastRowPointer'
            return False
        
        firstColPointer, lastColPointer = 0, noOfCols - 1
        while firstColPointer <= lastColPointer:
            middleColPointer = (firstColPointer + lastColPointer) // 2
            if target > matrix[middleRowPointer][middleColPointer]:
                firstColPointer = middleColPointer + 1
            elif target < matrix[middleRowPointer][middleColPointer]:
                lastColPointer = middleColPointer - 1
            else:
                return True
        return False

if __name__ == __main__:
    print("hello")