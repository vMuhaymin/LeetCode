class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        Sol is Log(n * m)
        """
        # row above, row below
        ra , rb = 0 , len(matrix) - 1

        # row mid
        rmid = (rb // 2)
        while ra <= rb :
            coll , colr = 0 , len(matrix[rmid]) - 1
            if matrix[rmid][0] == target :
                return True

            #Checking the left upper segament 
            elif matrix[rmid][0] < target :
                highest_row_num = len(matrix[rmid])-1
                if matrix[rmid][highest_row_num] >= target:
                    print("pass")
                    while coll <= colr :
                        cmid = ((coll + colr)//2)
                        if matrix[rmid][cmid] == target:
                            return True
                        elif matrix[rmid][cmid] < target:
                            coll = cmid + 1
                        else:
                            colr = cmid - 1
                    return False
                else:
                    #updating the mid
                    ra = rmid + 1
                    print(f'ra = {ra} , rb = {rb} , mid = {rmid}')

            #Checking the lower upper segament 
            else :
                highest_row_num = len(matrix[rmid])-1
                if matrix[rmid][highest_row_num ] >= target and matrix[rmid][0] <= target :
                    while coll <= colr :
                        cmid = ((coll + colr)//2)
                        if matrix[rmid][cmid] == target:
                            return True
                        elif matrix[rmid][cmid] < target:
                            coll = cmid + 1
                        else:
                            colr = cmid - 1
                    return False 
                else:
                    #updating the mid
                    rb = rmid - 1
            rmid = ((ra + rb) // 2)
        return False
                    