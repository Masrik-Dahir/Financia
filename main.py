def compound_value(amount, interest, year, dca, growth):
    times=1 + growth
    if year == 0:
        return amount
    amount = amount*times+amount*interest*times+dca
    return compound_value(amount, interest, year-1,dca, growth)

def hodl(dca, interest, year, growth):
    return compound_value(dca, interest, year, dca, growth)

print(hodl(dca=150,interest=0.062,year=20,growth=.1))
