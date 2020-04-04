def main():
    K = int(input())

    lunlun_number_memo = {}

    # def is_lunlun(str_n):
    #     while True:
    #         if lunlun_number_memo.get(str_n):
    #             return True
    #         elif len(str_n) == 1:
    #             return True
    #         else:
    #             if abs(int(str_n[0]) - int(str_n[1])) <= 1:
    #                 str_n = str_n[1:]
    #             else:
    #                 return False


    lunlun_number_count = 0
    i = 0
    while lunlun_number_count < K:
        i += 1
        # if is_lunlun(str(i)):
        str_i = str(i)
        while True:
            if lunlun_number_memo.get(str_i) or len(str_i) == 1:
                lunlun_number_memo[str(i)] = True
                lunlun_number_count += 1
                break
            else:
                if abs(int(str_i[0]) - int(str_i[1])) <= 1:
                    str_i = str_i[1:]
                else:
                    break

            # print(i)
            # print(lunlun_number_count)
            # print("running")

    print(i)

if __name__ == '__main__':
    main()