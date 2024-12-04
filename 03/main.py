a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]  

num = int(input("Choose a number: "))  #Prasa, lai ievada skailtli

new_list = [] #vaido jaunu sarakstu.

for i in a:    #Izvada skaitļus no a kas doti kursu saskaitot iznāk norāditais skaitlis 
    if i < num:
        new_list.append(i)

print(new_list) #Izvada jauno sarakstu.