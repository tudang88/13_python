import sys
from os import path
sys.path.append('/home/tudang/06_myprj/13_python/utils')
from debug_utils import stack_depth
from functools import lru_cache
# use lru_cache from standard library
@lru_cache(maxsize=None)
def fibonancy(n):
    # print("{indent}fibonancy({n}) called".format(indent="  " * stack_depth(), n = n))
    if n <= 2:
        return 1
    return fibonancy(n-1) + fibonancy(n-2)

# die when n too large, i.e: n = 1000
if __name__ == "__main__":
    # fibonancy(6)
    print("fibonacy({0})= {1}".format(6,fibonancy(6)))