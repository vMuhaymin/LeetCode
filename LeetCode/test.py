class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
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
                print(f"The highest is {matrix[rmid][highest_row_num ]} , the col mid is {rmid}")

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
                print(f"The highest is {matrix[rmid][highest_row_num ]} , the col mid is {rmid} and {matrix[rmid][0] }")
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
            


                    
sol  = Solution()
print(f"Does {3} exist? {sol.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3)}")