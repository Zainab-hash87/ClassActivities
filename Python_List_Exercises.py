# Python List Exercises

# 1. Creating a List

fruits = ("apple", "cherry", "grapes", "Mango", "orange")
print(fruits) 

# 2. Accessing Elements

colors = ["red", "blue", "green", "yellow", "purple"]
print("first element:", colors[0])
print("third element:", colors[2])
print("last element:", colors[4])

#3. Modifying a List

number = [10, 20, 30, 40, 50]
number[1] = 25
number[-1] = 60
print(number)

#4. List Slicing

names = ["alice", "bob", "charlie", "david", "Emma"]
subset = names[:3]
print(subset)

#5. Looping through a List

List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in List:
    print(item**item)

#List Methods: Append and Extend

cart = [] 
cart.append("milk")
cart.append("bread")
cart.append("eggs")
cart.extend(["butter", "cheese"])
print(cart)

#7. Finding Maximum and Minimum in a List
Numbers= [45, 22, 88, 56, 92, 33]
print("max_number:", max(Numbers))
print("min_number:", min(Numbers))

#8. Counting Occurrences
letter = ["a", "b",'a', 'c', 'b', 'a', 'd']
count_of_a = letter.count("a")
print("count of a:", count_of_a)

#9. List Comprehension
even = []
for x in range(11):
    if x % 2 == 0:
        even.append(x**2)

print(even)

#10. Removing Duplicates
nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_nums = list(set(nums))
print(unique_nums)

