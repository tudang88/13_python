import sys
from os import path
sys.path.append('/home/tudang/06_myprj/13_python/utils')
from debug_utils import stack_depth

def max_profit(daily_price, budget):
    # Initial state value
    cash_not_owning_share = budget # cash only state
    cash_owning_share = -float('inf') # cash and share state
    for price in daily_price:
        # compute for each transition
        # on state cash
        strategy_buy = cash_not_owning_share - price
        if (strategy_buy < 0) :
            # do not have enough money to buy
            # mark it as a penalty to avoid this option
            strategy_buy = -float('inf')
        strategy_avoid = cash_not_owning_share
        # on state cash and share
        strategy_sell = cash_owning_share + price
        strategy_hold = cash_owning_share
        # compute new state
        cash_not_owning_share = max(strategy_avoid, strategy_sell)
        cash_owning_share = max(strategy_buy, strategy_hold)
    # the last cash state will be the profit after budget deduction
    return cash_not_owning_share - budget
if __name__ == "__main__":
    print("The profit:{0}".format(max_profit([1, 5, 3, 9, 2, 3, 20, 1, 50, 1], 100)))