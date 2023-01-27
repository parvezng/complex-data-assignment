mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchnage_rate': 103.25
}

# Your Code Start from here
line = mobile_data['data'][5]
bdt_rate = int(float(line['price'].split()[0])*mobile_data['exchnage_rate'])
output = [line['name'],'is made in',line['made'],'. The Price is', line['price'],'which is almost equal to',str(bdt_rate), 'BDT']
print(" ".join(output))