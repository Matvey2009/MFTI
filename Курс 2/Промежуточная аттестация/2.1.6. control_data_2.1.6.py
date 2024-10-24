def sort_words_by_length(a):
    n = list(map(str, a.split()))
    arr = sorted(n, key=lambda x: (len(x), x))
    return arr
