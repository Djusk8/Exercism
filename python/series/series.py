def slices(series, length):

    if length > len(series):
        raise ValueError("length too big")
    elif length <= 0:
        raise ValueError("length should be > 0")

    return [series[i:i+length] for i in range(len(series)-length + 1)]

