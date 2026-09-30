# def big(lst):
#     for i in range(len(lst)):
#         if lst[i] > 0:
#             lst[i] = "big"
#     return lst
# print(big([7,-3,2,-1]))

# def positive(lst):
#     count = 0
#     for i in lst:
#         if i > 0:
#             count += 1
#     lst[len(lst)-1] = count
#     return lst
# print(positive([-1,1,1,1]))

# def sum(lst):
#     sum = 0
#     for i in lst:
#         sum += i
#     return sum
# print(sum([5,6,7,8]))

# def avg(lst):
#     sum = 0
#     avg = 0
#     count = 0
#     for i in lst:
#         sum += i
#         count += 1
#     avg = sum / count
#     return avg
# print(avg([5,6,7,8]))

# def leng(lst):
#     return len(lst)
# print(leng([1,2,3,4]))

# def min(lst):
#     if len(lst) == 0:
#         return False
#     min = lst[0]
#     for i in lst:
#         if i < min:
#             min = i
#     return min
# print(min([4,3,2,1]))

# def max(lst):
#     if len(lst) == 0:
#         return False
#     max = lst[0]
#     for i in lst:
#         if i > max:
#             max = i
#     return max
# print(max([1,2,3,4]))

# def ultimate(lst):
#     sum = 0
#     avg = 0
#     count = 0
#     min = lst[0]
#     max = lst[0]
#     for i in lst:
#         sum += i
#         count += 1
#         avg = sum / count
#         if i < min:
#             min = i
#         elif i > max:
#             max = i
#     print("sumTotal: " , sum , "average: " , avg , "min: " , min , "max: " , max , "length: " , len(lst))
#     return lst
# ultimate([37,2,1,-9])

def reverse(lst):
    for i in range(len(lst) // 2):
        lst[i], lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]
    return lst

print(reverse([37, 2, 1, -9]))