import itertools, functools 
list_of_lists = [[1, 2, 3], [4], [5, 6]]
list_of_lists = (itertools.chain(*list_of_lists))
