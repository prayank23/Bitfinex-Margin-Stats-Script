import requests

url = "https://api.bitfinex.com/v2/stats1/pos.size:1m:tBTCUSD:long/last"

longs = requests.request("GET", url)

temp1 = longs.text

tl_val = "{0:.2f}".format(float(temp1.split(",",1)[1][:-1]))


url = "https://api.bitfinex.com/v2/stats1/pos.size:1m:tBTCUSD:short/last"

shorts = requests.request("GET", url)

temp2 = shorts.text

ts_val = "{0:.2f}".format(float(temp2.split(",",1)[1][:-1]))


url = "https://api2.bitfinex.com:3000/api/v2/stats1/credits.size.sym:1m:fBTC:tBTCUSD/last"

shorts_funded = requests.request("GET", url)

temp3 = shorts_funded.text

sf_val = temp3.split(",",1)[1][:-1]
hs_val = float(ts_val)-float(sf_val)

print("{0:.2f}".format((float(tl_val)/(float(tl_val)+float(ts_val)))*100),"% Longs ------- ","{0:.2f}".format((float(ts_val)/(float(tl_val)+float(ts_val)))*100),"% Shorts")
print("")
print("Longs: ",tl_val," BTC")
print("Shorts: ",ts_val," BTC")
print("Hedged Shorts: ","{0:.2f}".format(hs_val)," BTC")
