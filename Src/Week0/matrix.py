blue = "\033[34m"
white = "\033[37m"

def matrix():
    matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    rows = len(matrix) # count # of rows
    for i in range(rows):
        col = len(matrix[i]) # count # of columns
        for x in range(col):
            print(matrix[i][x], end='')
        print(white)
    return