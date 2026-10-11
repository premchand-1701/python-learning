# text =  input("Enter a string: ")
# reverse = ""
# for ch in text:     #loop through each character in the string
#     reverse = ch + reverse 
# print("Reversed string:", reverse)


# text = input("Enter a string: ")
# reverse = text[::-1]
# if text == reverse:
#     print("palindrome")              #if the string is the same as its reverse, it's a palindrome
# else:
#     print("not palindrome")


# password = input("Enter a password: ")
# has_digit = False
# has_alpha = False
# for ch in password:                 #check if password has at least one digit and one alphabet
#     if ch.isdigit():
#         has_digit = True
#     if ch.isalpha():
#         has_alpha = True
#     if len(password) >= 8 and has_digit and has_alpha:
#         print("valid passwword")
#     else:
#         print("invalid password")

# numbers = [10, 20, 30, 40]
# total = 0
# for num in numbers:            #sum of numbers in a list
#     total += num
#     print(total)

# numbers =  [10,50,20,80,30]
# largest = numbers[0]
# for num in numbers:          #find the largest number in a list
#     if num>largest:
#         largest = num
# print("largest number is:", largest)


# numbers = [10,20,10,30,20,40]
# unique = []
# for  num in numbers:            #find unique numbers in a list
#     if num not in unique:
#         unique.append(num)
#         print(unique)


# a=[10,20,30,40]
# b=[20,40,50,60]
# common=[]
# for num in a:
#     if num in b:                 #find common numbers in two lists
#         common.append(num)
#         print(common)


# students = [
#     ["Ravi", 85, "CSE"],
#     ["Priya", 72, "ECE"],
#     ["Arjun", 91, "CSE"],
#     ["Sneha", 65, "IT"]
# ]
# for student in students:          # loop through each student in the list
#     name = student[0]
#     marks = student[1]
#     department = student[2]
#     print(name, marks, department)



# highest = [0]
# for student in students:
#     if student["marks"] > highest[0]:   #highest mark student
#         highest = student
#         print([highest])


# n = int(input("enter a number: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):             #print a triangle of numbers
#         print(j, end="")
#     print()


# n = int(input("enter number:"))
# marks = list(map(int,input().split()))
# highest = marks[0]
# lowest = marks[0]
# passed = 0
# for mark in marks:
#     if mark > highest:                   #find the highest marks(taking n number of marks)
#         highest = mark
#     if mark < lowest:
#         lowest = mark
#     if mark >=50:
#         passed += 1
# print("highest mark is:",highest)
# print("lowest mark is:",lowest)
# print("passed:",passed)


#Auto-sync test