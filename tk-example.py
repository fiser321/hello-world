count = 0
s = [1,2,3,4]

def clean(ss):
    return ss + 1
    # for i in range(ss):
    #     count += 1
    #     return  i + 1

ss = list(map(clean, s))
print(ss, count)
x =