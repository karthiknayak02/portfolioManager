from ariadne.asgi import GraphQL
from ariadne import make_executable_schema
from ariadne import QueryType

import robinhoodCloud.robin_stocks.robinhood as rh
import pprint
import schema


def login():
    # replace with env variable

    login_log = rh.login(username="karthiknayak02",
                         password="poKe'mon!02",
                         expiresIn=60*60*24,
                         by_sms=True)

    print(login_log['detail'])

    # rs.logout()


pp = pprint.PrettyPrinter(indent=4)
login()
# Create QueryType instance for Query type defined in our schema...
query = QueryType()


# ...and assign our resolver function to its "hello" field.
@query.field("hello")
def resolve_hello(_, info):
    request = info.context["request"]
    user_agent = request.headers.get("user-agent", "guest")
    return "Hello, %s!" % user_agent


@query.field("portfolio")
def resolve_portfolio(_, info):
    assets = rh.account.build_holdings_list()
    return assets


@query.field("schedules")
def resolve_schedules(_, info):
    schedules_data = rh.account.clean_schedules_data()
    return schedules_data


schema = make_executable_schema(schema.type_defs, query)
app = GraphQL(schema, debug=True)