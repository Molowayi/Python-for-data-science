import requests
r = requests.get("https://api.parrycarry.com/coin/flip")
print(r)
print(r.text)