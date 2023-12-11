import requests
def market_total(l, data):
    total = 0
    for i in l:
            total = total + data[str(i)]["market_value"]
    return total

def process_for_points(list, data):
    base = "https://api.torn.com/market/"
    base_market = "?selections=itemmarket" 
    base_bazaar = "?selections=bazaar" 
    api_key = "bmljZSB0cnkgOi0p"
    total_cost = 0
    print("%-20s %-20s %-15s %-15s %-4s" % ("item", "Market Price", "Lowest Market", "Lowest Bazaar", "Gap"))
    for i in list:
        #get the lowest price on the item market
        call = base + str(i) + base_market + "&key=" + api_key
        response = requests.get(call)
        lowest_price_market = response.json()['itemmarket'][0]['cost']

        #get the lowest prices on bazaars
        call = base + str(i) + base_bazaar + "&key=" + api_key
        response = requests.get(call)
        lowest_price_bazaar = response.json()['bazaar'][0]['cost']

        #set up print information
        name = data[str(i)]["name"]

        #buy within a variance of the market price
        m_value = data[str(i)]["market_value"]
        purchase_price = int(m_value * 1.01)
        postscript = "https://www.torn.com/imarket.php#/p=shop&type=" + str(i)
        
        if(lowest_price_bazaar <= purchase_price or lowest_price_market <= purchase_price):
            if(lowest_price_bazaar <= purchase_price):
                diff = m_value-lowest_price_bazaar
            else:
                diff = m_value-lowest_price_market
            print("%-20s %-20s %-15s %-15s %-4s" % (name, m_value, lowest_price_market, lowest_price_bazaar, diff))
            print("\t" + postscript)

        if(lowest_price_market < lowest_price_bazaar):
             total_cost += lowest_price_market
        else:
             total_cost += lowest_price_bazaar
    print("Cost of a set: " + str(total_cost))