import sys
from os import path
sys.path.append('/home/tudang/06_myprj/13_python/utils')
from debug_utils import stack_depth

def max_profit(daily_price):
    # Initial state value
    cash_not_owning_share = 0 # cash only state
    cash_owning_share = -float('inf') # cash and share state
    for price in daily_price:
        # compute for each transition
        # on state cash
        strategy_buy = cash_not_owning_share - price
        strategy_avoid = cash_not_owning_share
        # on state cash and share
        strategy_sell = cash_owning_share + price
        strategy_hold = cash_owning_share
        # compute new state
        cash_not_owning_share = max(strategy_avoid, strategy_sell)
        cash_owning_share = max(strategy_buy, strategy_hold)
    # the last cash state will be the profit
    return cash_not_owning_share
if __name__ == "__main__":
    print("The profit:{0}".format(max_profit([1, 5, 3, 9, 2, 3, 20, 1, 50, 1])))