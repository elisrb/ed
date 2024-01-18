sarscov = input()
print(len(sarscov))
influenza = input()
print(len(influenza))
result = 0
i = 0
while i < len(sarscov):
    j = 0
    comum = 0
    while j < len(influenza):
        i2 = i
        while i2 < len(sarscov) and j < len(influenza) and sarscov[i2] == influenza[j]:
            comum+=1
            i2+=1
            j+=1
        if comum > result:
            result = comum
        comum = 0
        j+=1
    i+=1
print(result)