import requests
import json
import sys


if len(sys.argv)!=2:
    sys.exit("Missing command-line prompt")

# Check that entry with command line is a float
try:
    factor = float(sys.argv[1])
except ValueError:
    sys.exit("Command line argument is not a number")

# Check that response is there
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    #print(json.dumps(response.json(), indent = 2))
    prices = response.json()
    result= (prices["bpi"]["USD"]["rate_float"])

except requests.RequestException:
    sys.exit("Error with json request")

print (f"${result*factor:,.4f}")


