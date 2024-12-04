""" Method 1 """

num = int(input("Give me a number to check: ")) #Izvada jautajumu lai izvelas skaitli kuru parbaudit
check = int(input("Give me a number to divide by: "))

if num % 4 == 0:                #Ja skaitlis dalās ar skaitli 4 un raksta ja jā tad dalas ar 4, bet ja nē tad tas ir nedalas .
    print(num, "is a multiple of 4")
elif num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")

if num % check == 0:  
    print(num, "divides evenly by", check)
else:
    print(num, "doesn't divide evenly by", check)

""" Method 2 """              #prasa ievadit skaitli un spreiž vai tas ir nepāra skaitlis vai para skaitlis.
num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("You picked an odd number.")
else:
    print("You picked an even number.")
