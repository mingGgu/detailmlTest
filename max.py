def max(a,b):
    r = a
    if b > a:
        r = b
    return r

print(max(5,7))
#-- 결과 --
# 7

max = lambda a,b : a if a>b else b
print(max(50,30))
#-- 결과 --
# 50

def add(a,b):
    r = a + b
    return r

add = lambda a,b: a + b
print(add(5,8))
# --결과--
# 13

