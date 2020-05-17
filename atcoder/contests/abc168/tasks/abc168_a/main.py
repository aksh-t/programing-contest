def main():
    N = int(input())

    ones_place = N % 10

    if ones_place in [2, 4, 7, 5, 9]:
        print('hon')
    elif ones_place in [0, 1, 6, 8]:
        print('pon')
    else:
        print('bon')

if __name__ == '__main__':
    main()