def main():
    S = input()
    # S = "1" * 200000
    S = S[::-1]

    x = 1
    tot = 0
    cnt = [0] * 2019
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
        tot = (tot + (int(S[i]) * x)) % 2019
        ans += cnt[tot]
        x = (x * 10) % 2019
    
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