def main():
    N = int(input())
    S = input()

    R_count = 0
    G_count = 0
    B_count = 0

    for s in S:
        if s == "R":
            R_count += 1
        elif s == "G":
            G_count += 1
        else:
            B_count += 1

    # 第一条件だけを考えたときの組み合わせの総数
    answer = R_count * G_count * B_count

    # この二重ループが O(N^2)
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            # i, j が決まると、第二条件を満たさない k が決まる
            k = 2 * j - i

            # k が文字列の長さを超えたときは、第二条件を満たすことができない
            if k >= N:
                continue

            # 第二条件を満たす i, j, k が、第一条件を満たす場合、
            # 第一条件だけ考えたときの組み合わせの総数から差し引く
            if S[i] != S[j] and S[i] != S[k] and S[j] != S[k]:
                answer -= 1
            
    print(answer)

if __name__ == '__main__':
    main()