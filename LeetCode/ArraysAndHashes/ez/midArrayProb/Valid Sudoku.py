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

        
        square = {0}
        rowStart = 0
        while rowStart <= 6:

            for i in range(3,9,3):
                for j in range(rowStart,i):
                    if board[rowStart][i] != ".":
                        num = int(board[rowStart][i])
                        print(num)
                        if num in square:
                            print(num)
                            return False
                        else:
                            square.add(num)
                square = {0}
            rowStart += 3

        
        return True



sol = Solution()
res = sol.isValidSudoku([[".",".",".",".","5",".",".","1","."],
                         [".","4",".","3",".",".",".",".","."],
                         [".",".",".",".",".","3",".",".","1"],
                         ["8",".",".",".",".",".",".","2","."],
                         [".",".","2",".","7",".",".",".","."],
                         [".","1","5",".",".",".",".",".","."],
                         [".",".",".",".",".","2",".",".","."],
                         [".","2",".","9",".",".",".",".","."],
                         [".",".","4",".",".",".",".",".","."]]
)

print(f"The result is {res}")


    

    

     
