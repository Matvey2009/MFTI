n = [input() for i in range(int(input()))]
print(len([i for i in n if n.count(i) > 1]))
