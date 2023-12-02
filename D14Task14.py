import requests

# 1 REST COUNTRIES API

data2 = requests.get('https://restcountries.com/v3.1/all')
if data2.status_code == 200:
    datas = data2.json()

    for d in datas:
        name =d['name']['common']
        currency = d.get('currencies','no currency')
        print(f"Name= {name}\ncurrency= {currency}")


data = requests.get('https://restcountries.com/v3.1/all')
if data.status_code == 200:
    datas = data.json()

    for d in datas:
        name =d['name']['common']
        currency = d.get('currencies','no currency')
        # print(f"Name= {name}\ncurrency= {currency}")

        
        
        if currency == {'EUR': {'name': 'Euro', 'symbol': '€'}}:
            print(f'\nEuro using countries={name}')
    
else:
    print("Error")



data1= requests.get('https://restcountries.com/v3.1/all')
if data1.status_code == 200:
    datas = data1.json()

    for d in datas:
        name =d['name']['common']
        currency = d.get('currencies','no currency')
        # print(f"Name= {name}\ncurrency= {currency}")

        if currency == {'USD': {'name': 'United States dollar', 'symbol': '$'}}:
            print(f'\nDollar using countries= {name}')

else:
    print("Error")



# 2. BEWERY API

import requests


data1 = requests.get("https://api.openbrewerydb.org/v1/breweries")
if data1.status_code == 200:
    datas = data1.json()
    
    for b in datas:  
        state =b['state']
        brewerry = b['brewery_type']
        if state == "Alaska" or state =="Maine" or state == "New York":
            print(f"Brewery-type={brewerry}")
