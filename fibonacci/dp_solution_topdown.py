import sys
from os import path
sys.path.append('/home/tudang/06_myprj/13_python/utils')
from debug_utils import stack_depth


fibonancy_cache = {}
def fibonancy(n):
    # print("{indent}fibonancy({n}) called".format(indent="  " * stack_depth(), n = n))
    if n <= 2:
        return 1
    # only recursive for item not calculated yet
    # otherwise takes from cache
    if n not in fibonancy_cache:
        fibonancy_cache[n] = fibonancy(n-1) + fibonancy(n-2)
    return fibonancy_cache[n]

# die when n too large, i.e: n = 1000
if __name__ == "__main__":
    print("fibonacy({0})= {1}".format(100,fibonancy(100)))