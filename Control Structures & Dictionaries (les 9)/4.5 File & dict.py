def ticker(content):
    ticker = input('Enter Ticker symbol: ')
    for line in lines:
        company_split = line.split(':')
        if company_split[1].replace('\n', '') == ticker:
            ticker_dict = {company_split[0]: company_split[1]}
            return ticker_dict
    return None

file = open('/Users\Jake\Desktop/Ticker.txt', 'r+')
lines = file.readlines()
ticker_symbol = ticker(lines)
if ticker_symbol != None:
    for k in ticker_symbol.keys():
        print('Ticker Symbol: ' + k)
else:
    print('No combinations found.')