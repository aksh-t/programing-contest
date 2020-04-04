N, M = map(int, input().split())

As = list(map(int,input().split()))
vote_sum = sum(As)
least_vote_num = vote_sum / (4 * M)

if len([A for A in As if A >= least_vote_num]) >= M:
    print('Yes')
else:
    print('No')