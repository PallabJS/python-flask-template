from os import system
import time
import hashlib
import hmac

import config


def getTimeStamp():
    return str(int(time.time_ns()/1000000))


def composeQueryString(timestamp, **kwargs):
    # eg. symbol=symbol&limit=2
    query = ""
    for key in kwargs:
        query = query + f"{key}={kwargs[key]}&"

    if timestamp:
        return f"{query}timestamp={getTimeStamp()}"
    else:
        return query[0: len(query)-1]


def getUri(signed, timestamp, symbol, endpoint, **kwargs):
    query_string = composeQueryString(timestamp, symbol=symbol, **kwargs)

    if signed:
        # Create the signature from query_string
        signature = hmac.new(key=config.secret_key.encode(encoding="utf-8"),
                             msg=query_string.encode(encoding="utf-8"),
                             digestmod=hashlib.sha256).hexdigest()
        return f"{config.wazirx}/{endpoint}?{query_string}&signature={signature}"
    else:
        return f"{config.wazirx}/{endpoint}?{query_string}"
