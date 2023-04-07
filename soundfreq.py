import decimal




def stdfreq(musictune):
    bi = decimal.Decimal(2)**decimal.Decimal(1/12)
    freq = decimal.Decimal(523)
    stdtune = {'A': -3,
               'A#': -2,'Bb':-2,
               'B':-1,
               'C':0,
               'C#':1,'Db':1,
               'D':2,
               'D#':3,'Eb':3,
               'E':4,
               'F':5,
               'F#':6,'Gb':6,
               'G':7}
    tunechange = int(stdtune[musictune])
    if tunechange != 0:
        freq = freq * (bi**tunechange)
    
    freq = freq * (bi**(-36))

    freqs = []
    for i in range(84):
        freqs.append(int(freq.quantize(decimal.Decimal('0'))))
        freq = freq*bi
    # print(freqs[36])
    return freqs

if __name__ == "__main__":
    stdfreq('C')

