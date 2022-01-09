numbers = [1, 2, 3, 4, 5, 6, 7]
numbers2 = []

for i in numbers:
    numbers2.append(i ** 2)
print(numbers2)

# řešení pynative
#  numbers = [1, 2, 3, 4, 5, 6, 7]
# result list
# res = []
# for i in numbers:
    # calculate square and add to the result list
    # res.append(i * i)
# print(res)

# druhé řešení
# numbers = [1, 2, 3, 4, 5, 6, 7]
# res = [x * x for x in numbers]
# print(res)