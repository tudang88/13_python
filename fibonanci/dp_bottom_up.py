import sys
from os import path
sys.path.append('/home/tudang/06_myprj/13_python/utils')
from debug_utils import stack_depth


def fibonancy(n):
    # print("{indent}fibonancy({n}) called".format(indent="  " * stack_depth(), n = n))
    series = [1,1]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return series[-1]

# by getting rid of stack over flow error, this method could 
# run with n > 1000 without any issue
# but this approach still consumes too much memories for saving all series
if __name__ == "__main__":
    # fibonancy(6)
    print("fibonacy({0})= {1}".format(1000,fibonancy(1000)))