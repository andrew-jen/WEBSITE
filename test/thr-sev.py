from collections import Counter
def findMode(ns):
    counts = Counter(ns)
    mode = counts.most_common(1)[0][0]
    return mode
