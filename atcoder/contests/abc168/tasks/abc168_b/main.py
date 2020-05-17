def main():
    K = int(input())
    S = input()

    if len(S) > K:
        print(f'{S[:K]}...')
    else:
        print(S)

if __name__ == '__main__':
    main()