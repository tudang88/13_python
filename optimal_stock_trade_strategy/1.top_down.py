import sys
from os import path
sys.path.append('/home/tudang/06_myprj/13_python/utils')
from debug_utils import stack_depth
from functools import lru_cache

def max_profit(daily_price):
    #caching the result
    @lru_cache(maxsize=None)
    def get_best_profit(day_nth, have_stock):
        """Return the best profit that can be obtained by the end of the day.
        At the end of the day:
        * if have_stock is True, the trader must own the stock;
        * if have_stock is False, the trader must not own the stock.
        """
        print("{indent}get_best_profit({n}) have_stock={flag} called".format(indent="  " * stack_depth(), n = day_nth, flag = have_stock))
        if day_nth < 0:
            # Initial state: no stock and profit
            if not have_stock:
                return 0
            else:
                # we are not allowed to have initial stock.
                # Add a very large penalty to eliminate this option.
                return -float('inf')
        # obtain price of the day
        price = daily_price[day_nth]
        if have_stock:
            # We can reach this state by buying or selling
            strategy_buy = get_best_profit(day_nth-1, False) - price # sell on previous day, then buy today
            strategy_sell = get_best_profit(day_nth -1, True) + price # buy on previous day, then sell today
            return max(strategy_buy, strategy_sell)
        else:
            # we can reach this state by selling or avoid
            strategy_sell = get_best_profit(day_nth-1, True) + price # buy on previous day, then sell today
            strategy_avoid = get_best_profit(day_nth -1, False) # sell on privious day, avoid today
            return max(strategy_sell, strategy_avoid)
    
    # Final state: end of last day, no shares owned
    last_day = len(daily_price) - 1
    no_stock = False
    return get_best_profit(last_day, no_stock)


if __name__ == "__main__":
    max_profit([1,5,3,9,2,3])