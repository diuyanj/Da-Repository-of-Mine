def diamond(n):
    R = 0
    _R = n

    while R < n * 2 - 1:
        x = n - R
        if x <=0: x -= 2
        for _ in range(abs(x)):
            print(" ", end="")
        if R < n:
            for i in range(R+1):
                print(i+1, end="")
            if R > 0:
                for i in range(R):
                    print(R-i, end="")
        else:
            _R -= 1
            for i in range(_R):
                print(i+1, end="")
            for i in range(_R-1):
                print(_R-i-1,end="")
        R+= 1
        print("")

diamond(7)










        # current_int = d-d+1
        # ascend = True
        # if i+1 < d:
        #     for _ in range(d-i):
        #         print(" ", end="")
        # if i != 0:
        #     print(d-current_int, end="")
        # print(i+1, end="")
        # if i+1 == d:
        #     ascend = False
        # current_int += 1
        # if i != 0:
        #     print(d-current_int)
        # print("")

        # if i+1 < d:
        #     print(i+1, end="")







#     for n in range(d - _num + 1):
#         if n < d:
#             print(" ", end="")
#     if _num > 0:
#         ascend(_num, d)
#     if _num <= 0:
#         descend(_num)

# def ascend(_num, d):
#     for n in range(d):
#         print(_num - d + n + 1, end="")

# def descend(d):
#     pass




#     while R < n * 2 - 1:
#         create_space(R, n)
#         if R < n:
#             for i in range(R+1):
#                 print(i+1, end="")
#         if R >= n:
#             for i in range(n - (abs(n - R)) - 1):
#                 print(i+1, end="")
#         R += 1
#         print("")
#         # print(f"R = {R}")

# def create_space(R, n):
#     x = n - R
#     for _ in range(abs(x)):
#         print(" ", end="")