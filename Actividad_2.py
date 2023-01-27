tp = (1, "David", 3.1416, "135D", 79846)
print(tp)
ltp = list(tp)
print(ltp)
dic = {}
for i in ltp:
    ind = ltp.index(i)+1
    dic[ind] = i

print(dic)
print(dic.keys())
print(dic.values())