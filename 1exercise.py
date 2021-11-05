N = int(input("Write a number:"))

sum_of_odd = 0 
sum_of_even = 0
evennumber = 0

for i in range(0,N+1): 
    if i%2 == 1:
        sum_of_odd += i
    if i%2 == 0 :
        sum_of_even += i
        evennumber += 1
print("sum of odd numbers: {}".format(sum_of_odd))
print("average of even numbers: {}".format(sum_of_even / evennumber))
        
        

    
   

