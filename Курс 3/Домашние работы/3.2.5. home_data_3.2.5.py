def bin_ip(iparr):
    di = {}
    for i in iparr:
        k = ''.join(format(int(j), '08b') for j in i.split('.'))
        di[k] = i
    return {k: v for k, v in sorted(di.items())}
