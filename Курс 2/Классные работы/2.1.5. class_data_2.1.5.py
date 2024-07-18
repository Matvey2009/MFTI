a = input()
b = int(input())
print(a[0]*((b-len(a))//2)+a+a[-1]*((b-len(a))//2)+"."*(b-len(a[0]*((b-len(a))//2)+a+a[-1]*((b-len(a))//2))))
