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


def generate_new(new_login=False):


    login()

    holdings = rh.account.build_holdings_list()
    holdings_pd = pd.DataFrame(holdings)
    holdings_pd.to_csv("/Users/tank/projects/portfolioManager/holdings_data.csv")
    # pp.pprint(holdings)

    positions_data = rh.account.get_open_stock_positions()
    # pp.pprint(positions_data[0])
    positions_data_pd = pd.DataFrame(positions_data)
    positions_data_pd = rh.data_clean_helper.clean_position_data(positions_data_pd)
    positions_data_pd.to_csv("/Users/tank/projects/portfolioManager/positions_data.csv")

    schedules_data = rh.account.clean_schedules_data()
    # pp.pprint(schedules_data[0])
    schedules_data_pd = pd.DataFrame(schedules_data)
    schedules_data_pd.to_csv("/Users/tank/projects/portfolioManager/schedules_data.csv")

    positions_plus = pd.merge(holdings_pd, schedules_data_pd, on='symbol')
    schedules_data_pd.to_csv("/Users/tank/projects/portfolioManager/positions_plus.csv")


if __name__ == '__main__':

    import schema

    pp = pprint.PrettyPrinter(indent=4)

    holdings_pd = pd.read_csv('holdings_data.csv')

















