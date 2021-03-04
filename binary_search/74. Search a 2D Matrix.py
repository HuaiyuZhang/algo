# solution 1
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    nrows = len(matrix)
    ncols = len(matrix[0])
    total = nrows * ncols
    l = 0
    r = total - 1
    while l <= r:
        mid = l + (r - l)//2
        row_idx = mid // ncols
        col_idx = mid % ncols 
        num = matrix[row_idx][col_idx]
        if num == target:
            return True
        elif num < target:
            l = mid + 1
        else:
            r = mid - 1
    return False

# solution 2
def find_row(self, matrix, target):
        l = 0
        r = len(matrix) - 1
        while l <= r:
            mid = l + (r - l)//2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                return mid
            if target < matrix[mid][0]:
                r = mid - 1
            else:
                l = mid + 1
        return -1
    
def find_col(self, matrix_row, target):
    l = 0
    r = len(matrix_row) - 1
    while l < r:
        mid = l + (r - l+1)//2
        if target < matrix_row[mid]:
            r = mid - 1
        else:
            l = mid
    return matrix_row[l] == target

def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    return self.find_col(matrix[self.find_row(matrix, target)], target)
