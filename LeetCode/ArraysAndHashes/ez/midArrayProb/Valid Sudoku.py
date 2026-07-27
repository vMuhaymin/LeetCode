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
        
        return True



sol = Solution()
res = sol.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])

print(f"The result is {res}")


    

    

     
