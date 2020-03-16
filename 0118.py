# 33
'10 10'
'####*****@'
'@#@@@@#*#*'
'@##***@@@*'
'#****#*@**'
'##@*#@@*##'
'*@@@@*@@@#'
'***#@*@##*'
'*@@@*@@##@'
'*@*#*@##**'
'@****#@@#@'
'0 0'

# 29
'9 10'
'####*****@'
'@#@@@@#*#*'
'@##***@@@*'
'#****#*@**'
'##@*#@@*##'
'*@@@@*@@@#'
'***#@*@##*'
'*@@@*@@##@'
'*@*#*@##**'
'0 0'

# 29
'10 9'
'####*****'
'@#@@@@#*#'
'@##***@@@'
'#****#*@*'
'##@*#@@*#'
'*@@@@*@@@'
'***#@*@##'
'*@@@*@@##'
'*@*#*@##*'
'@****#@@#'
'0 0'

hw = input().split()
h = int(hw[0])
w = int(hw[1])

divisions = [list(input()) for i in range(h)]
end = input()
if end != '0 0':
    raise AssertionError('InputParseError')


def dfs(x, y, kind):
    if divisions[x][y] == kind:
        divisions[x][y] = '.'

        if 0 <= x - 1 < h:
            dfs(x - 1, y, kind)
        if 0 <= x + 1 < h:
            dfs(x + 1, y, kind)
        if 0 <= y - 1 < w:
            dfs(x, y - 1, kind)
        if 0 <= y + 1 < w:
            dfs(x, y + 1, kind)

def solve():
    res = 0
    for x_index in range(h):
        for y_index in range(w):
            kind = divisions[x_index][y_index]
            if kind != '.':
                dfs(x_index, y_index, kind)
                res = res + 1
    print(res)

solve()
