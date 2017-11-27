from collections import Counter
import re


def find_most_frequent(a):
    a=a.lower()
    a=re.sub(r'[^\w\s]',' ',a)
    li=a.split(' ')
    cnt=Counter()
    l=[]
    for w in li:
        cnt[w] += 1
    l=[key for key, val in cnt.items() if val==max(cnt.values())]
    l.sort()
    return l


print(find_most_frequent(input()))