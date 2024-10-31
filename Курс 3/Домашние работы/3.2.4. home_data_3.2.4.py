def backpack(pr, maxi):
    so = sorted(pr, key=lambda x: pr[x], reverse=True)
    maxi*=1000
    to, ba = 0, []
    for i in so:
        if to + pr[i] <= maxi:
            ba.append(i)
            to += pr[i]
    return ba
