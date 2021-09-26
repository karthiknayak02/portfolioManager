import pandas as pd

def clean_position_data(positions: pd.DataFrame) -> pd.DataFrame:
    """
    Takes PD dataframe with full position data provided from robinhood
    Then cleans out to get relevant info we want to keep
    """

    # Delete multiple columns from the dataframe
    positions = positions.drop(["url", "instrument", "account", "account_number", "pending_average_buy_price",
                                "intraday_average_buy_price", "intraday_quantity", "shares_available_for_exercise",
                                "shares_held_for_buys", "shares_held_for_sells", "shares_held_for_stock_grants",
                                "shares_held_for_options_collateral", "shares_held_for_options_events",
                                "shares_pending_from_options_events", "shares_available_for_closing_short_position",
                                "ipo_allocated_quantity", "ipo_dsp_allocated_quantity", "avg_cost_affected"], axis=1)

    positions['updated_at'] = pd.to_datetime(positions['updated_at']).dt.date
    positions['created_at'] = pd.to_datetime(positions['created_at']).dt.date

    return positions
