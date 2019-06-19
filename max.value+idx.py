"""code bit."""


def maxval(data):
    """Return  list of index and value of maximum values in data."""
    maxvals = []
    for idx in range(len(data)):
        item = data[idx]
        if (len(maxvals)) == 0:
            maxvals.append((idx, item))
        elif item == maxvals[0][1]:
            maxvals.append((idx, item))
        elif item > maxvals[0][1]:
            maxvals = [item]
    return maxvals


go = [1, 4, 6, 46]
maxval(go)
