def triple_diff(a, b, c, s=True):
    if s:
        return a.symmetric_difference(b).symmetric_difference(c)
    else:
        return a.difference(b).difference(c)
