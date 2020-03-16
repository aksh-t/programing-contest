'2 700'
'3 500'
'5 800'


first_line_params = input().split()
D = int(first_line_params[0])
G = int(first_line_params[1])

task_list = []
c_list = []

for d in range(D):
    params = input().split()
    p = int(params[0])
    s = (d + 1) * 100
    c = int(params[1])
    c_list.append((s, p, c)) 

    for i in range(p):
        task_list.append(s)

print(task_list)
print(c_list)


def dfs(i, res, score, clear_list):
    clear_list.append(task_list[i])
    res = res + 1
    score = score + task_list[i]
    c_score = 0
    for c in c_list:
        if clear_list.count(c[0]) == c[1]:
            c_score = c_score + c[2]
    if score + c_score >= G:
        return res
    else:
        res = dfs(i+1, res, score, clear_list)
        if res:
            return res 
            
    res = dfs(i+1, res, score, clear_list)
    if res:
        return res 

def solve():
    res = dfs(0, 0, 0, [])
    print(res)

solve()

