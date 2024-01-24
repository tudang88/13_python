import sys
from os import path
sys.path.append('/home/tudang/06_myprj/13_python/utils')
from debug_utils import stack_depth


def fibonancy(n):
    # print("{indent}fibonancy({n}) called".format(indent="  " * stack_depth(), n = n))
    previous = 1
    current = 1
    for i in range(n-2):
        next = current + previous
        previous, current = current, next
    return current

# by saving only the last two elements, we saving a lot of memory compare to the previous method
if __name__ == "__main__":
    # fibonancy(6)
    print("fibonacy({0})= {1}".format(1000,fibonancy(2000)))