
## This script uses the dictionary utility of the python and counts the number of the characters in the string 
def Counter(str):
    d=dict()
    for c in str:
        if c not in d:
            d[c]=1
        else :
            d[c]=d[c]+1

    return  d


## Yahoo is the sample string 
temp=Counter("Yahoo")
print temp