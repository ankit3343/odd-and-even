x=eval(input("Enter a lists: "))
count_even=0
count_odd=0
for i in x:
    if i%2==0:
        count_even=count_even+1
    else:
        count_odd=count_odd+1
print('even numbers are', count_even)
print('odd numbers are', count_odd)