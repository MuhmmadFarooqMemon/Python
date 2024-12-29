# Program to print numbers from 1 to 10 using for loop
print("For Loop")
for i in range(1, 11):
    print(i)

# Program to print numbers from 1 to 10 using while loop
print("While Loop")
i = 1
while i <= 10:
    print(i)
    i += 1


# Program using break to stop the loop when user enters 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        print("Stopping the program.")
        break
    print("You entered:",num)


# Program using continue to skip number 5
for i in range(1, 11):
    if i == 5:
        continue  # Skip the rest of the loop for number 5
    print(i)



# Program to print prime numbers from 1 to 20 using else in for loop
for num in range(2, 21):  # Loop through numbers from 2 to 20
    for i in range(2, num):  #Nested Loop 
        if num % i == 0:
            break  # If divisible by any number, it's not prime
    else:
        print(num,"Is A Prime Number")  # If not divisible by any number, it's prime
