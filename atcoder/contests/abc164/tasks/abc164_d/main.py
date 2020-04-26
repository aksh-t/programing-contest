def main():
    S = input()

    # MAX_S = int("9" * 200000) # 大き過ぎる
    multipuls = []
    # answers = []
    answer = 0

    for i in range(1, 10000):
        multipuls.append(str(2019 * i))

    for multipul in multipuls:
        answer += S.count(multipul)

    # for i in range(len(S) - 1):
    #     for j in range(i + 3, len(S)):
    #         # print(S[i:j+1])
    #         # print(i + 1, j + 1)
    #         if int(S[i:j+1]) % 2019 == 0:
    #             answers.append((i + 1, j + 1))

    # print(len(answers))
    print(answer)


if __name__ == '__main__':
    main()