def dsort(d, reverse=False):
    return dict(sorted(d.items(), key=lambda x: x[0], reverse=reverse))
