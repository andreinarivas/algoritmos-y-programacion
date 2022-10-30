symbols={'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
currency=(input('Please enter a currency: ')).capitalize()
print(symbols.get(currency, "Not in repertory"))