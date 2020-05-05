def main():
    X = int(input())
    deposit = 100

    i = 0
    while True:
        deposit = int(deposit * 1.01)
        i += 1

        if deposit >= X:
            print(i)
            exit()

if __name__ == '__main__':
    main()