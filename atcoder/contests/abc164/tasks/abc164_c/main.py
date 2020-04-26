def main():
    N = int(input())
    S_set = set()

    for i in range(N):
        S_set.add(input())

    print(len(S_set))

if __name__ == '__main__':
    main()