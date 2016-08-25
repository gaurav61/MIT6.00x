# PROBLEM 1 : Counting Vowels
count=0
for char in s:
    if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
        count+=1
print count



# PROBLEM 2 : Counting Bobs
count=0
for i in range(0,len(s)-2):
    if s[i]=='b' and s[i+1]=='o' and s[i+2]=='b':
         count+=1
print count


# PROBLEM 3 : Counting and Grouping
def item_order(order):
    count1=order.count('salad',0,len(order))
    count2=order.count('hamburger',0,len(order))
    count3=order.count('water',0,len(order))
    return 'salad:'+str(count1)+' hamburger:'+str(count2)+' water:'+str(count3)
