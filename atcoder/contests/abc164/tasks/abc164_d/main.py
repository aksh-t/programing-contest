from collections import defaultdict

def main():
    S = input()
    # S = "1" * 200000
    S = S[::-1]

    x = 1
    tot = 0
    cnt = defaultdict(int)
    ans = 0

    for i in range(len(S)):
        # print("-----")
        # print(f"i: {i}")
        # print(f"tot: {tot}")
        # print(f"S[i]: {S[i]}")
        # print(f"x: {x}")
        # print(f"cnt: {cnt}")
        # print(f"cnt[tot]: {cnt[tot]}")
        # print(f"ans: {ans}")

        cnt[tot] += 1
        tot += int(S[i]) * x
        tot %= 2019
        ans += cnt[tot]
        x = x * 10
    
    # print("-----")
    # print(f"i: {i}")
    # print(f"tot: {tot}")
    # print(f"S[i]: {S[i]}")
    # print(f"x: {x}")
    # print(f"cnt: {cnt}")
    # print(f"cnt[tot]: {cnt[tot]}")
    # print(f"ans: {ans}")
    
    print(ans)


if __name__ == '__main__':
    main()