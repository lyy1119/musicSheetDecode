import decimal


bi = decimal.Decimal(2)**decimal.Decimal(1/12)

def stdfreq():
    # 低
    pre = decimal.Decimal(523)
    freq = decimal.Decimal(523)

    pre = freq
    sharp_freq = []
    freqs = []
    for i in range(24):
        print(freq)
        freqs.append(int(freq.quantize(decimal.Decimal('0'))))
        freq = freq*bi


    print(freqs)

