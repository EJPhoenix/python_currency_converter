# COUNTRY AND EXCHANGE RATED BASED ON USD
currency_dict = {
    'USD': 1,
    'GBP': 0.79,
    'EUR': 0.92,
    'AUS': 1.52,
    'CAD': 1.34,
    'SGD': 1.34,
    'CHF': 0.87,
    'MYR': 4.77,
    'JPY': 150.23,
    'RMB': 7.19
}
print(currency_dict)


def currency_converter():
    # USERS STARTING CURRENCY
    source_currency = input('What currency are you exchanging? ').upper()
    while source_currency not in currency_dict:
        source_currency = input('Try again. What currency are you exchanging?: ').upper()
        print(source_currency)

    # USERS TARGET CURRENCY
    target_currency = input('What currency do you want to receive? ').upper()
    while target_currency not in currency_dict:
        target_currency = input('Try again. What currency are you exchanging?: ').upper()
        print(target_currency)

    # AMOUNT OF SOURCE CURRENCY BEING EXCHANGED
    try:
        input_amount = float(input('How much does you want to exchange? '))
        while input_amount <= 0:
            input_amount = float(input('Invalid entry. Please try again: '))
    except ValueError:
        print("Invalid entry. Please restart")
        exit()

    # ACCESS TARGET->USD EXCHANGE RATE
    source_to_usd_exchange_rate = currency_dict[source_currency]
    # print(source_to_usd_exchange_rate)

    # CONVERTING SOURCE CURRENCY TO USD
    to_usd = input_amount / source_to_usd_exchange_rate

    # CONVERTING FROM USD TO TARGET CURRENCY
    to_target_currency = to_usd * currency_dict[target_currency]
    rounded_final_currency = round(to_target_currency, 3)

    print(f"You exchanged: {input_amount} {source_currency}\nWhich equals: {rounded_final_currency} {target_currency}")


currency_converter()
