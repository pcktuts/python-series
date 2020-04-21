# Lambda Function in python
def double(x):
    return x * x
print(double(10))

d = lambda x, y: x * y # lambda argugements: expression
print(d(10, 8))
my_list = [1, 2, 3, 4, 5 , 6, 7, 8 , 9, 10]
my_even_list = list(filter(lambda x: (x %2 == 0), my_list))
print(my_even_list)
my_double_list = list(map(lambda  x: x * x, my_list))
print(my_double_list)

def lambda_squre(l, x):
    return l(x)
l = lambda x: x * x
print(lambda_squre(l, 10))
