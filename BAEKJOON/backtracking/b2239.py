
def sudoku(n):
    global row, col, square, mat, ans, flag
    if flag:
        return

    if n == 81:
        flag = 1
        for line in range(9):
          print(''.join(map(str, mat[line])))
        return

    i = n//9
    j = n%9
    sq = i//3 * 3 + j//3

    if not mat[i][j]:
        for x in range(1, 10):
            if not row[i][x] and not col[j][x] and not square[sq][x]:
                row[i][x] = 1
                col[j][x] = 1
                mat[i][j] = x
                square[sq][x] = 1
                sudoku(n + 1)
                mat[i][j] = 0
                row[i][x] = 0
                col[j][x] = 0
                square[sq][x] = 0
    else:
        sudoku(n+1)

mat = [list(map(int, list(input()))) for _ in range(9)]


row = [[0] * 10 for _ in range(9)]
col = [[0] * 10 for _ in range(9)]
square = [[0] * 10 for _ in range(9)]
ans = 0
flag = 0

for i in range(9):
    for j in range(9):
        if mat[i][j]:
            row[i][mat[i][j]] = 1
            col[j][mat[i][j]] = 1
            square[i//3 * 3 + j//3][mat[i][j]] = 1
sudoku(0)

