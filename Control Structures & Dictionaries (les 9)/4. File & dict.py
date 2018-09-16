def ticker(content):
    company = input('Enter company name: ')
    for line in lines:
        company_split = line.split(':')
        if company_split[0] == company:
            company_dict = {company_split[0]: company_split[1]}
            return company_dict
    return None

file = open('/Users\Jake\Desktop/Ticker.txt', 'r+')
lines = file.readlines()
ticker_symbol = ticker(lines)
if ticker_symbol != None:
    for v in ticker_symbol.values():
        print('Ticker Symbol: ' + v)
else:
    print('No combinations found.')