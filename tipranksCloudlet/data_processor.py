import requests
import statistics
import time
from datetime import datetime, date, time, timezone
import pprint
import json
from tipranksCloudlet.urls import *
from dateutil.relativedelta import relativedelta



THREE_MONTHS = 90
days_per_unit = {"d": 1, "w": 7, "m": 30, "y": 365}

def convert_to_days(time):
    return int(time[:-1]) * days_per_unit[time[-1]]

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

"""
 Get price targets of symbol
 @param symbol
 @returns {Promise.<TResult>}
"""
def getPriceTargets(symbol: str):
    query = {'name': 'AMZN'} #, 'benchmark': '1', 'period': 3, 'break': time.time()}
    response = requests.get(base_url() + 'getData/', params=query)
    resp_obj = response.json()

    sum = 0
    estimates = []
    t = {
        'mean': 0,
        'median': 0,
        'highest': 0,
        'lowest': float('inf'),
        'numberOfEstimates': 0
    }

    for consensuses in resp_obj['consensuses']:
        date_of_rating = consensuses['d']
        print(date_of_rating)
        price_target = consensuses['priceTarget']
        three_months = date.today() + relativedelta(months=-3)
        parsed_date = datetime.strptime(date_of_rating, "%d/%m/%y")
        print(parsed_date)

        # if three_months < time.strptime(date_of_rating, "%d/%m/%y").date() < date.today() and price_target:
        #     t['highest'] = price_target if price_target > t['highest'] else t['highest']
        #     t['lowest'] = price_target if price_target < t['lowest'] else t['lowest']
        #     t['numberOfEstimates'] += 1
        #     estimates.append(price_target)
        #     sum += price_target

    # for experts in resp_obj['experts']:
    #     # print(experts['ratings'])
    #     days_of_rating = experts['ratings'][0]['d']
    #     price_target = experts['ratings'][0]['priceTarget']
    #     # print(convert_to_days(days_of_rating))
    #     # print(experts['ratings'][0]['time'])
    #
    #     if convert_to_days(days_of_rating) < THREE_MONTHS and price_target:
    #         print(experts['ratings'])
    #         t['highest'] = price_target if price_target > t['highest'] else t['highest']
    #         t['lowest'] = price_target if price_target < t['lowest'] else t['lowest']
    #         t['numberOfEstimates'] += 1
    #         estimates.append(price_target)
    #         sum += price_target

    t['mean'] = sum / t['numberOfEstimates']
    t['median'] = statistics.median(estimates)
    print(t)

    # try:
    #     response = requests.get('http://api.open-notify.org/astros.json', timeout=5)
    #     response.raise_for_status()
    #     # Code here will only run if the request is successful
    # except requests.exceptions.HTTPError as errh:
    #     print(errh)
    # except requests.exceptions.ConnectionError as errc:
    #     print(errc)
    # except requests.exceptions.Timeout as errt:
    #     print(errt)
    # except requests.exceptions.RequestException as err:
    #     print(err)

    return


# def clean_position_data(positions: pd.DataFrame) -> pd.DataFrame:
#     """
#     Takes PD dataframe with full position data provided from robinhood
#     Then cleans out to get relevant info we want to keep
#     """
#
#     # Delete multiple columns from the dataframe
#     positions = positions.drop(["url", "instrument", "account", "account_number", "pending_average_buy_price",
#                                 "intraday_average_buy_price", "intraday_quantity", "shares_available_for_exercise",
#                                 "shares_held_for_buys", "shares_held_for_sells", "shares_held_for_stock_grants",
#                                 "shares_held_for_options_collateral", "shares_held_for_options_events",
#                                 "shares_pending_from_options_events", "shares_available_for_closing_short_position",
#                                 "ipo_allocated_quantity", "ipo_dsp_allocated_quantity", "avg_cost_affected"], axis=1)
#
#     positions['updated_at'] = pd.to_datetime(positions['updated_at']).dt.date
#     positions['created_at'] = pd.to_datetime(positions['created_at']).dt.date
#
#     return positions


if __name__ == '__main__':

    getPriceTargets("AMZN")