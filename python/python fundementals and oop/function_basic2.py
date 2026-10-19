# def countdown(num):
#     output = []
#     for i in range(num, -1, -1):
#         output.append(i)
#     return output

# print(countdown(5))
    
# def print_return(lst):
#     print(lst[0])
#     return lst[1]
# print(print_return([2,1]))

# def first_length(lst):
#     output = lst [0] + len(lst)
#     return output
# print(first_length([1,5,3,4,2]))

# def values_greater_than_second(lst):
#     if len(lst)<2:
#         return False
#     else:
#         output=[]
#         second=lst[1]
#         for i in lst:
#             if i>second:
#                 output.append(i)
                
#     print(len(output))
#     return output
# print(values_greater_than_second([5,2,3,2,1,4]))

def value_size(size, value):
    output = []
    for i in range(size):
        output.append(value)  
    return output
print(value_size(5,7))