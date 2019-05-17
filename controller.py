#!/usr/bin/env python3

import model
import view

def game_loop():
    while True:
        user_input    = view.main_menu().lower()
        buy_inputs    = ["b", "buy"]
        sell_inputs   = ["s", "sell"]
        lookup_inputs = ["l", "lookup"]
        quote_inputs  = ["q", "quote"]
        exit_inputs   = ["e", "exit"]

        acceptable_inputs = buy_inputs     \
                            +sell_inputs   \
                            +lookup_inputs \
                            +quote_inputs  \
                            +exit_inputs

        if user_input in acceptable_inputs:
            if user_input in buy_inputs:
                # FIXME
                # State of the Program:
                ## User wants to buy stock
                ### company referred to by TICKER SYMBOL
                #### global unique identifiers

                ## What we should try to do next (ie sudo code)
                ##   --trader_name
                ##   --ticker_symbol
                ##   --trade_volume
                ##   --limit_price --> coming from `view`
                ##   --time_stamp --> defined in `model`
                ## "we're building out the order ticket"

                (username, password) = view.login_menu()
                (ticker_symbol, trade_volume) = view.buy_menu()
                #######################################


                with model.User(username) as u:
                    if u.login(password):
                    # excute the buy order,
                    # if there's enough money in acct
                        confirmation_message = u.buy(ticker_symbol, trade_volume)
                        print (confirmation_message)
                    pass


                pass
            elif user_input in sell_inputs:
                # FIXME
                pass


if __name__ == "__main__":
    print (game_loop())
