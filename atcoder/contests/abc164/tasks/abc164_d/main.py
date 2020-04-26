def main():
    S = input()

    # MAX_S = int("9" * 200000) # 大き過ぎる
    multipuls = []
    answers = []

    i = 1
    while True:
        if 2019 * i > MAX_S:
            print(i)
            break
        multipuls.append(2019 * i)
        i += 1
        print(i, 2019 * i)

    # for i in range(len(S) - 1):
    #     for j in range(i + 3, len(S)):
    #         # print(S[i:j+1])
    #         # print(i + 1, j + 1)
    #         if int(S[i:j+1]) % 2019 == 0:
    #             answers.append((i + 1, j + 1))

    # print(len(answers))


if __name__ == '__main__':
    main()