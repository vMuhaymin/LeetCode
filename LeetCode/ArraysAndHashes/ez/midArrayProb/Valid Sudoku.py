class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        print("Hola")

        row = {0}
        col = {0}

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = int(board[i][j])
                    if num in row:
                        return False
                    else:
                        row.add(num)
            row = {0}
            for k in range(9):
                if board[k][i] != ".":
                    numCol = int(board[k][i])
                    if numCol in col:
                        return False
                    else:
                        col.add(numCol)
            col = {0}

        prev = 0
        bCol = 3
        bRow = 3
        square = {0}
        while bCol != 12 and bRow != 12:
            for i in range(prev,bCol):
                for j in range(prev,bRow):
                    if board[i][j] != ".":
                        num = int(board[i][j])
                        if num in square:
                            return False
                        else:
                            square.add(num)
            
            prev = bCol
            bCol += 3 
            bRow +=3
            square = {0}
        
        return True



sol = Solution()
res = sol.isValidSudoku(
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8","2","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])

print(f"The result is {res}")


    

    

     
