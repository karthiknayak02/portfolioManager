import robinhoodCloud.robin_stocks.robinhood as rh
import pprint
from datetime import datetime
import pandas as pd


ONE_DAY = 60 * 60 * 24  # in seconds


def login():
    # replace with env variable

    login_log = rh.login(username="karthiknayak02",
                         password="poKe'mon!02",
                         expiresIn=ONE_DAY,
                         by_sms=True)

    print(login_log['detail'])

    # rs.logout()


if __name__ == '__main__':

    import schema

    pp = pprint.PrettyPrinter(indent=4)

    login()

    holdings = rh.account.build_holdings_list()
    pp.pprint(holdings)

    positions_data = rh.account.get_open_stock_positions()
    # pp.pprint(positions_data[0])
    positions_data_pd = pd.DataFrame(positions_data)
    positions_data_pd.to_csv("/Users/tank/projects/portfolioManager/positions_data.csv")

    schedules_data = rh.account.clean_schedules_data()
    # pp.pprint(schedules_data[0])
    schedules_data_pd = pd.DataFrame(schedules_data)
    schedules_data_pd.to_csv("/Users/tank/projects/portfolioManager/schedules_data.csv")


