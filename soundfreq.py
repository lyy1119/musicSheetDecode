import decimal


bi = decimal.Decimal(2)**decimal.Decimal(1/12)



# 低
pre = decimal.Decimal(523)
freq = decimal.Decimal(523)
for i in range(12*3):
    freq = freq/bi
pre = freq
sharp_freq = []
freqs = []
for i in range(4):
    for j in range(1 , 13):
        if j == 1 or j == 3 or j == 5 or j == 6 or j == 8 or j == 10 or j == 12:
            freqs.append(int(str(freq.quantize(decimal.Decimal('0')))))
        else:
            sharp_freq.append(int(str(freq.quantize(decimal.Decimal('0')))))
        freq = freq*bi


print(freqs)

print(sharp_freq)
