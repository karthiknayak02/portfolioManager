"""Contains all the url endpoints for interacting with Robinhood API."""

def base_url():
    return 'https://www.tipranks.com/api/stocks/'


def challenge_url(challenge_id):
    return('https://api.robinhood.com/challenge/{0}/respond/'.format(challenge_id))

def orders_url(orderID=None):
    if orderID:
        return('https://api.robinhood.com/orders/{0}/'.format(orderID))
    else:
        return('https://api.robinhood.com/orders/')
