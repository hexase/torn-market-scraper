import requests
from functions import *

api_key = "bmljZSB0cnkgOi0p"
plushies = [186,187,215,618,261,258,273,266,268,269,274,281,384]
flowers = [260,263,272,617,264,271,267,282,277,276,385]
other = []

interested_items = plushies + flowers + other

interested_items_string = "".join(str(i) + "," for i in interested_items)
info_call = "https://api.torn.com/torn/" + interested_items_string + "?selections=items&key=" + api_key

data_response = requests.get(info_call)
data = data_response.json()["items"]

response = requests.get(info_call)

process_for_points(plushies, data)
process_for_points(flowers, data)


print("Market Cost of Plushie Set: " + str(market_total(plushies, data)))
print("Market Cost of Flower Set:  " + str(market_total(flowers, data)))