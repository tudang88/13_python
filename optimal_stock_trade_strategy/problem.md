# Problem: Optimal stock market strategy

* Write an algorithm that, given the daily price of a stock, computes the maximum profit that can be made by buying or selling that stock. Assume that you are allowed to own no more than 1 share at any time, and that you have an unlimited budget.

# Analysis
* Given
  * an array of daily price of a stock
  * you are allowed to own no more than 1 share at any time.
  * You have unlimited budget.
* Action
  * Compute the maximum profit can be made by either
    * selling
    * buying
* Solution
  * Clarifying that at the end of each day, the state we could have will be one of the following states
    * Cash: (sell the share, own cash)
    * cash + share: (buy a share and remain some cashs)
  * And the possible transitions between two days
    * avoid: do not buy share, keep the cash (cash -> cash)
    * buy: buy a share (cash -> cash + share)
    * sell: sell the share, own cash (cash + share -> cash)
    * hold: hold the share (cash + share -> cash + share)

# Problem variation 1: limited investment budget
* In a variation of the original problem, the investment budget is limited: 
  * we start with a fixed amount of money
  * We are not allowed to buy a share if we cannot affort it
    * means we do not have enough cash amount to buy a certain share
* Solution:
  * The solution for this variation only including a contrain on buy transition (if the amount of money < price, do not buy)