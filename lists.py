# Lists
# A list is a relationship of indices and elements
# A map between an element and its postion

[1,2,3,4,5,6] # list of integers

["Gensi",12 ,45 ,78 ,'a'] #list of strings and integers

coffee = ["arabica", "robusta", "morgus", "liberica"]

type(coffee)

# working with a list that has numbers
# printing out the elements

# numbers = [1,2,3,4,5]
# for num in numbers:
#     print(num)

# print("")

# updating a list
# numbers = [69,27,32,45,28]
# for marks in range(len(numbers)):
#     marks = marks + 10
#     print(marks)



# numbers = [69,27,32,45,28]
# for marks in numbers:
#     marks = marks + 10
#     print(marks)




#creating an empty list
empty=[]

for i in empty:
    print(i)

# adding lists using concactenation operators
num1 = [1,2,3,4]
num2 =[ 6,7,8,9]
num3 = num1 + num2
print(num3)

# multiplying lists by integers
num4 = [1,2]
num5 = num4 * 2
print(num5)

# working with indices in lists
cs_performance = [56,78,87,96,57,90,67]
first_3 = cs_performance[1:3]
print(first_3)

print(cs_performance[4:])

print(cs_performance[3:6])

print(cs_performance[:]) #this will print from the first index to the last index 

# changing elements of the list using slices
cs_performance[1:3] = [60,50]
print(cs_performance)

# adding elements at hte end of the list
cs_performance.append(87)
print(cs_performance)

# using extend function to add two lists
cw_perf = [34,45,44,21]

cs_performance.extend(cw_perf)
print(cs_performance)
