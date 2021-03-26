# map
liste = [1,2 ,3 ,4 ,5 ]
print(list(map(lambda x: x* 10, liste)))

# filter
liste = [1,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,1 ,0]
print(list(filter(lambda x: x % 2 == 0, liste)))

# reduce
from functools import reduce
liste = [1,2 ,3 ,4 ]
print(reduce(lambda a,b : a + b, liste))










