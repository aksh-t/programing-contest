def main():
    N = int(input())
    S = input()

    answer = 0

    for i in range(N - 2):
        Si = S[i]
        for j in range(i + 1, N - 1):
            Sj = S[j]
            if Si == Sj:
                continue

            for k in range(j + 1, N):
                Sk = S[k]
                if Si == Sk or Sj == Sk:
                    continue
                if j - i == k - j:
                    continue
                answer += 1
    print(answer)

if __name__ == '__main__':
    main()