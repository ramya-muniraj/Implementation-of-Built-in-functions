def my_abs(number):
    """implementation of built-in 'abs'function"""
    if number<0:
        return (-number)
    else:
        return (number)

print(my_abs(-20.0))


def my_all(iterable):
    """implementation of built-in 'all' function"""
    value=1
    for i in iterable:
        if i==False:
           value=0
           break

    if value==0:
        print("False")
    else:
        print("True")
    return i    
lst=[1,10,20,0]
print(my_all(lst))


def my_divmod(a,b):
     """implementation of built-in 'divmod' function"""
     q=a//b
     r=a%b
     print("("+str(q) +","+str(r) +")")
my_divmod(5,4)    


def my_len(s):
    """implementation of built-in 'len' function"""
    count=0
    for i in s:
       count=count+1
    print(count)
my_len('adc')     


def my_max(lst):
    """implementation of built-in 'max' function"""
    max=0
    for i in lst:
        if i>max:
            max=i
    print (max)
my_max([2,2,20])      


def my_pow(base,exponent):
    """implementation of built-in 'pow' function"""
    print( base**exponent)
my_pow(2,1)


def my_reverse(s):
    """implementation of built-in 'reverse' function"""
    return( s[::-1])
text=my_reverse("how are you")    
print(text)

def my_sorted(lst,revese=False):
    """implementation of built-in 'sort' function"""
    temp=0
    
    for i in range(0,len(lst)):
        for j in range(i+1,len(lst)):
            if (lst[i]>lst[j]):
                temp=lst[i]
                lst[i]=lst[j]
                lst[j]=temp
    

    print("elements of original list:",lst)
    
my_sorted([5,2,7,11,8])


def my_sum(lst):
    """implementation of built-in 'sum' function"""
    x=0
    for i in lst:
        x=x+i
    print( x)
my_sum([10,20,30])
        


            
            
   
        
