from common import *

"""
 Get price targets of symbol
 https://www.tipranks.com/api/stocks/getData/?name=NET
"""
def get_price_targets_consensus(symbol: str):
    request_url = "https://www.tipranks.com/api/stocks/getData/"
    query_params = {'name': symbol}
    response = get_call(request_url=request_url, query_params=query_params)

    value = None
    schema = {
        "ticker": value,
        "companyName": value,
        "ptConsensus": [
            [0],
            {
                "priceTarget": value,
                "high": value,
                "low": value
            }],
        "latestRankedConsensus": {
            "rating": value,
            "nB": value,
            "nH": value,
            "nS": value
        }
    }

    price_targets = parse_response(schema, response)
    print(price_targets)
    return price_targets


"""
 Get basic stock details
 # https://market.tipranks.com/api/details/getstockdetailsasync?id=AMZN
"""
def get_stock_details(symbol: str):
    request_url = "https://market.tipranks.com/api/details/getstockdetailsasync"
    query_params = {'id': symbol}
    response = get_call(request_url=request_url, query_params=query_params)

    value = None
    schema = [
        [0],
        {
            "ticker": "AMZN",
            "price": value,
            "pe": value,
            "eps": value,
            "marketCap": value,
            "yLow": value,
            "yHigh": value,
            "nextEarningDate": value,
            "range52Weeks": value,
            "low52Weeks": value,
            "high52Weeks": value
        }
    ]

    stock_details = parse_response(schema, response)
    print(stock_details)
    return stock_details


if __name__ == '__main__':
    get_price_targets_consensus("AMZN")
    get_stock_details("AMZN")
