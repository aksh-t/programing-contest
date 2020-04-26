def main():
    S = input()
    multipuls = []
    answers = []

    # 事前に2019の倍数を作っておいた方がコスト削減になるかと思ったが、
    # あまり意味がない気がしてきたのでやめる
    # i = 1
    # while True:
    #     if 2019 * i > 200000:
    #         break
    #     multipuls.append(2019 * i)
    #     i += 1

    for i in range(len(S) - 1):
        for j in range(i + 3, len(S)):
            # print(S[i:j+1])
            # print(i + 1, j + 1)
            if int(S[i:j+1]) % 2019 == 0:
                answers.append((i + 1, j + 1))

    print(len(answers))


if __name__ == '__main__':
    main()