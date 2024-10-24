rows = int(input("Enter The number of Rows: "))
number = 1

for x in range(1,rows+1):
    for i in range(x):
        print(number,end=" ")
        number += 1 
    print()
    
