# PROBLEM  1 : 
def isPalindrome(aString):
   if len(aString)<=1:
      return True
   return aString[0]==aString[-1] and isPalindrome(aString[1:-1])
   
 
   
# PROBLEM  2 :
def dotProduct(listA, listB):
    pro=0
    for i in range(0,len(listA)):
        pro=pro+(listA[i]*listB[i])
    return pro
    
    
# PROBLEM  3 :
def flatten(aList):
    if aList == []:
        return aList
    if isinstance(aList[0], list):
        return flatten(aList[0]) + flatten(aList[1:])
    return aList[:1] + flatten(aList[1:])
    
    
# PROBLEM  4 :
def dict_interdiff(d1, d2):
    a1={}
    a2={}
    for i in d1:
        for j in d2:
            if i==j:
                a1.update({i:f(d1[i],d2[i])})
    for i in d1:
        flag=0
        for j in d2:
            if i==j:
                flag=1
        if flag==0:
            a2.update({i:d1[i]})
    for i in d2:
        flag=0
        for j in d1:
            if i==j:
                flag=1
        if flag==0:
            a2.update({i:d2[i]})
    #print a1
    #print a2
    return (a1,a2)
    
    
# PROBLEM  5 :
def satisfiesF(L):
    count=0
    l1=L[0:]
    for i in l1:
        if f(i)==True:
           count+=1
        else:
            L.remove(i)
    
    return count
run_satisfiesF(L, satisfiesF)



