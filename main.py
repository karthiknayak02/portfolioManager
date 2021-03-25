import robin_stocks.robinhood as rh
import pprint
from datetime import datetime
import pandas as pd

ONE_DAY = 60 * 60 * 24  # in seconds


def clean_schedules_data(schedules):
    """Returns a list containing every position ever traded.

    :param schedules: Will filter the schedules to get a specific values
    :type schedules: Optional[list]
    :returns: [list] Returns a list of dictionaries of key/value pairs for each ticker. If info parameter is provided, \
    a list of strings is returned where the strings are the value of the key that matches info.
    :Dictionary Keys: * url
                      * instrument
                      * account
                      * account_number
                      * average_buy_price
                      * pending_average_buy_price
                      * quantity
                      * intraday_average_buy_price
                      * intraday_quantity
                      * shares_held_for_buys
                      * shares_held_for_sells
                      * shares_held_for_stock_grants
                      * shares_held_for_options_collateral
                      * shares_held_for_options_events
                      * shares_pending_from_options_events
                      * updated_at
                      * created_at
    """
    # pp.pprint(schedules[0]) # to look at input
    refined_schedule_list = []

    for schedule in schedules:

        original_equity_price = 'None'
        if schedule['original_equity_price']:
            original_equity_price = schedule['original_equity_price']['amount']

        new_schedule_details = {'instrument_id': schedule['investment_target']['instrument_id'],
                                'symbol': schedule['investment_target']['instrument_symbol'],
                                'amount': schedule['amount']['amount'],
                                'frequency': schedule['frequency'],
                                'next_investment_date': schedule['next_investment_date'],
                                'total_invested': schedule['total_invested']['amount'],
                                'state': schedule['state'],
                                'schedule_updated_at': schedule['updated_at'][:10],  # truncated time
                                'schedule_created_at': schedule['created_at'][:10],  # truncated time
                                'schedule_first_investment_date': schedule['first_investment_date'],
                                'schedule_first_investment_price': original_equity_price,
                                'schedule_id': schedule['id'],
                                'source_of_funds': schedule['source_of_funds'],
                                'start_date': schedule['start_date']}

        def replace_none_with_none_str(any_dict):
            return {k: ('None' if v is None else v) for k, v in any_dict.items()}

        new_schedule_details = replace_none_with_none_str(new_schedule_details)
        refined_schedule_list.append(new_schedule_details)

    return refined_schedule_list


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def login():
    # replace with env variable

    login_log = rh.login(username="karthiknayak02",
                         password="poKe'mon!02",
                         expiresIn=ONE_DAY,
                         by_sms=True)

    print(login_log['detail'])

    # rs.logout()


if __name__ == '__main__':
    print_hi('PyCharm')
    pp = pprint.PrettyPrinter(indent=4)

    login()

    sample0 = rh.account.get_all_positions()[0]

    # pp.pprint(sample0)

    positions_data = rh.account.get_all_positions()

    schedules_full = rh.account.get_all_auto_investment()

    schedule_data = clean_schedules_data(schedules_full)

    pp.pprint(schedule_data[0])

    testing = pd.DataFrame(schedule_data)

    print(testing)

    print(rh.order_buy_limit('AAPL', 1, 55.77))

    testing.to_csv("/Users/tank/projects/robinhood/aloha.csv")

    # for item in positions_data:
    #     print(rh.get_symbol_by_url(item['instrument']))
    #
    #     print(rh.get_name_by_url(item['instrument']))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
# Request URL: https://api.robinhood.com/auto_investment/schedules/next_investment_date/?frequency=weekly&start_date=2021-03-11
# :path: /auto_investment/schedules/next_investment_date/?frequency=weekly&start_date=2021-03-11
#
# path: /instruments/450dfc6d-5510-4d40-abfb-f633b7d9be3e/recurring_tradability
# https://bonfire.robinhood.com/instruments/2bbdb493-dbb1-4e9c-ac98-6e7c93b117c0/recurring_tradability"
# history/2bbdb493-dbb1-4e9c-ac98-6e7c93b117c0
