import sys
import queue

def main():
    K = int(input())
    q = queue.Queue()
    for i in range(1, 10):
        q.put(i)

    i = 0
    while True:
        i += 1

        n = q.get()
        center_num = (10 * n) + (n % 10)
        
        if n % 10 != 0:
            q.put(center_num - 1)
        
        q.put(center_num)

        if n % 10 != 9:
            q.put(center_num + 1)

        if i >= K:
            # print(q.queue)
            print(n)
            sys.exit()

if __name__ == '__main__':
    main()