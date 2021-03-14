# report.py
import csv

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            stock = {
                 'name'   : row[0],
                 'shares' : int(row[1]),
                 'price'   : float(row[2])
            }
            portfolio.append(stock)

    return portfolio

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices

def make_report_data(portfolio, prices):
    report = [(*list(p.values())[:-1], prices[p['name']], prices[p['name']] - p['price']) for p in portfolio]
    return report

def portfolio_report(portfolio_filename, prices_filename):

    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report_data(portfolio, prices)

    total_cost = 0.0
    for s in portfolio:
        total_cost += s['shares'] * s['price']
    print('Total cost', total_cost)
    
    total_value = 0.0
    for s in portfolio:
        total_value += s['shares'] * prices[s['name']]
    print('Current value', total_value)
    
    print('Gain', total_value - total_cost)

    headers = ('Name', 'Shares', 'Price', 'Change')
    print(' '.join([f'{header:>10s}' for header in headers]))
    print(' '.join(['-' * 10] * 4))
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {f"${price:.2f}":>10s} {change:>10.2f}')
    for row in report:
        print('%10s %10d %10.2f %10.2f' % row)


portfolio_report('Work/Data/portfolio.csv', 'Work/Data/prices.csv')