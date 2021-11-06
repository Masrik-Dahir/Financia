def compound_value(amount, interest, month, dca, growth):
    if month == 1:
        return amount
    else:
        amount = amount * (1 + growth)
        # print(amount)
        # print(amount * interest)
    amount = amount + amount * interest + dca

    return compound_value(amount, interest, month - 1, dca, growth)


def dca_year(dca, interest, year, growth):
    return compound_value(dca, interest, year, dca, growth)


def dca_month(dca, interest, month, growth):
    interest = interest * (1 / 12)
    growth = growth * (1 / 12)
    return compound_value(dca, interest, month, dca, growth)


def invest(principle, interest, month, growth):
    interest = interest * (1 / 12)
    growth = growth * (1 / 12)
    return compound_value(principle, interest, month, 0, growth)


print(dca_month(1000, .1, 12, 0.5))
print(invest(1000, .1, 12, 0.5))
