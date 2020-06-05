
array = [13, 4, 9, 5, 3, 16, 12] #<-- Create an array of number 

def selectionSort(array): #<-- Define a function to sort array 

    n = len(array) #<-- Define "n" as the length of the array 

    for i in range(n): #<--Whatever the length of the array is how many times you are going to run the for loop 

        #Initally assume the first element of the unsorted part as the minimun

        minimum = i #<-- Define minumun as i 

        for j in range(i+1, n):
            #Move the smallest value up first
            if(array[j] < array[minimum]): #<--Comparision Operator
            
        #Swap the minimum element with the first element of the unsorted part 
        temp = array[i] #<--Temporary value: a place holder to substitute value later on 
        array[i] = array[minimum] #<-- Create user input array elements to be equal to the minimum element
        array[minimum] = temp #<-- Create a temporary placement for the minimum elements 

    return array #<-- Calling the array 

print(selectionSort(array)) #<-- Print selection array 