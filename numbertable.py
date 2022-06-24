import time
print("The Number table calculator! Enter any natural number and enjoy it's table! ")
num = int(input("Enter the number you want the table of: "))
print(":) here you go")
for i in range(num,num*21,num):
    time.sleep(1)
    print(f"{i}")



