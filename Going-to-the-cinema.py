# kata 562f91ff6a8b77dfe900006e
from math import ceil


def movie(card, ticket, perc):
    price_a = 0
    price_b = card
    previous_price = ticket * perc
    c = 0
    while ceil(price_b) >= price_a:
        price_a += ticket
        price_b += previous_price
        previous_price *= perc
        c += 1
    print(c)


movie(500, 15, 0.9)  # 43
movie(100, 10, 0.95)  # 24
