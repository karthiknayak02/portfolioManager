from ariadne import gql
from ariadne import *

type_defs = gql("""
    type Query {
        portfolio: [Asset]
        hello: String!
        schedules: [Schedule]!
    }

    type Asset {
        average_buy_price: Float!
        equity: Float!
        equity_change: Float!
        id: ID!
        name: String!
        percent_change: Float!
        percentage: Float!
        price: Float!
        quantity: Float!
        symbol: String!
        type: String!
    }
    
    scalar Date
    
    type Schedule {   
        amount: Float!
        frequency: String!
        instrument_id: ID!
        next_investment_date: Date!
        schedule_created_at: Date!
        schedule_first_investment_date: Date!
        schedule_first_investment_price: Float!
        schedule_id: ID!
        schedule_updated_at: Date!
        source_of_funds: String!
        start_date: Date!
        state: String!
        symbol: String!
        total_invested: Float!
    }
    
    """)
