#print(range(10))

# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i*2)
#     return result
#
# my_list = make_list(100)
# print(my_list)


def generator_function(num):
    for i in range(num):
        yield i*2
for item in generator_function(100):
    print(item)