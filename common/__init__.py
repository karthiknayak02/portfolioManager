import requests

"""
 Gets values from response with specified schema
"""
def parse_response(schema, response):

    if type(schema) is list:
        for i in schema[0]:
            schema[i + 1] = parse_response(schema[i + 1], response[i])
        schema.pop(0)

    if type(schema) is dict:
        for key, value in schema.items():
            if key in response:
                if not value:
                    schema[key] = response[key]
                if type(value) is dict:
                    schema[key] = parse_response(schema[key], response[key])
                if type(value) is list:
                    for i in value[0]:
                        schema[key][i+1] = parse_response(schema[key][i+1], response[key][i])
                    value.pop(0)
            else:
                print(key + " not in response object")

    return schema


def get_call(request_url, query_params, timeout_sec=5):
    try:
        response = requests.get(request_url, params=query_params, timeout=timeout_sec)
        resp_obj = response.json()
        response.raise_for_status()
        # Code here will only run if the request is successful

        return resp_obj

    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)

    return


