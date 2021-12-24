import time
import json
from requests import request
import config
from wazirx_api.api import getUri

from core.response.response_template import ResponseTemplate


class Order():
    @staticmethod
    def getOrders(symbols, limit) -> ResponseTemplate:
        res = ResponseTemplate()
        orders = []
        try:
            for symbol in symbols:
                endpoint = "uapi/v1/allOrders"
                api_uri = getUri(signed=True,
                                 timestamp=True,
                                 symbol=symbol,
                                 endpoint=endpoint,
                                 limit=limit,
                                 recvWindow=10000)
                response = request(url=api_uri,
                                   method="GET",
                                   headers={"X-Api-Key": config.api_key})

                # DEBUG STATEMENT
                # print(f"order response for {symbol}: \
                #      {json.dumps(response.json(), indent=2)}")

                if(response.status_code == 200):
                    orders.extend(response.json())

            res.setStatus(success=True, data=orders)
        except Exception as e:
            print(e)
            res.setStatus(error=True, msg=str(e))
        return res

    @staticmethod
    def getProfits(orders):
        res = ResponseTemplate()
        profits = []
        for order in orders:
            # Breathe between every 2 requests
            if(orders.index(order) % 1 == 0):
                time.sleep(0.5)

            total_buy_price = float(order['price']) * float(order['origQty'])
            ticker_uri = getUri(signed=False,
                                timestamp=False,
                                endpoint="sapi/v1/ticker/24hr",
                                symbol=order['symbol'])
            response = request(url=ticker_uri, method="GET",
                               headers={"X-Api-Key": config.api_key})

            if(response.status_code != 200):
                print("skipped")
                continue

            ticker_data = response.json()
            currentValue = float(order['origQty']) * \
                float(ticker_data['lastPrice'])
            profit = currentValue - total_buy_price
            profits.append({
                "symbol": order['symbol'],
                "investedValue": total_buy_price,
                "currentValue": currentValue,
                "profit": profit
            })

        all_symbols = [data['symbol'] for data in profits]
        all_symbols = list(set(all_symbols))

        profits_combined = []
        total_profit = {
            "totalInvested": 0,
            "totalProfit": 0
        }

        result_profit = {}

        for symbol in all_symbols:
            result_profit[symbol] = {
                "symbol": symbol,
                "investedValue": 0,
                "currentValue": 0,
                "profit": 0
            }
            for profit in profits:
                if(profit['symbol'] == symbol):
                    result_profit[symbol]["investedValue"] += profit['investedValue']
                    result_profit[symbol]['profit'] += profit['profit']
                    result_profit[symbol]["currentValue"] += profit['currentValue']

                    total_profit['totalInvested'] += profit['investedValue']
                    total_profit['totalProfit'] += profit['profit']

            # profit per symbol
            profits_combined.append(result_profit[symbol])

        # Overall profit calculation
        profits_combined.append(total_profit)

        res.setStatus(success=True, data=profits_combined)
        return res
