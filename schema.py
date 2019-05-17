#!/usr/bin/env python3


## TODO create pseudo-code in this schema file to layout tables needed for the terminal trader


## table names:
## users
## transaction history
## positions

## TABLE users:
#   1) pk
#   2) usernames
#   3) passwords
#   4) (cash?)

## TABLE transaction history:
#   1) pk
#   2) usernames
#   3) ticker
#   4) trade_volume
#   5) side (buy vs sell)
#   6) execution_price
#   7) execution time (system time?)
#   8) ?? foreign key ??


## TABLE positions/market value:
#   1) pk
#   2) username
#   3) ticker
#   4) qty
#   5) avg_price
#   6) mkt_value (for each symbol in each person's portfolio) --mkt value of what they *paid*
#   7) ?? foreign key ??
