from sys import exit

def main():
    K = int(input())
    A, B = map(int, input().split())

    # for i in range(A, B + 1):
    #     if i % K == 0:
    #         print("OK")
    #         exit()

    # print("NG")

    if A % K == 0:
        print("OK")
        exit()
    
    if B // K > A // K:
        print("OK")
    else:
        print("NG")

if __name__ == '__main__':
    main()