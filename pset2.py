# PROBLEM 1 : Paying the Minimum
sum=0.0
month=0
for i  in range(0,12):
       month+=1
       payment=balance*(monthlyPaymentRate)
       balance=balance-payment
       balance=balance+(annualInterestRate/12.0)*balance
       print ('Month: '+str(month))
       print ('Minimum monthly payment: %.2f' % payment)
       print ('Remaining balance: %.2f' % balance)
       sum=sum+payment
print ('Total paid: %.2f' % sum)
print ('Remaining balance: %.2f' % balance)


# PROBLEM 2 : Paying Debt Off in a Year
minpay=0
totalpay=balance
while totalpay>0:
    totalpay=balance
    minpay+=10
    for i in range(0,12):
        totalpay=totalpay-minpay
        totalpay=totalpay+(totalpay*(annualInterestRate/12.0))
print ('Lowest payment: '+str(minpay))


# PROBLEM 3 : Using Bisection Search to Make the Program Faster
def fun(a,b,c):
    for i in range(0,12):
        a=a-c
        a=a+(a*(b/12.0))
    return a    
low=balance/12.0
up=(balance * ((1 + (annualInterestRate/12)) ** 12)) / 12
mid=(low+up)/2.0
arr=0.00001
curr_bal=fun(balance,annualInterestRate,mid)
while abs(curr_bal)>arr:
    if curr_bal<0:
        up=mid
    else:
        low=mid
    mid=(low+up)/2.0
    curr_bal=fun(balance,annualInterestRate,mid)
print ('Lowest Payment: %.2f' %mid)
