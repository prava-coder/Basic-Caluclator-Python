#write  a program to make a simple caluclator by using the if else
print("lets starat to perform the basic caluclation operations")
print("select operation")
print("1.addition")
print("2.subraction")
print("3.multiplication")
print("4.division")
while True:
    #taking input from the user
    select_choice=input("enter your choice(1/2/3/4):")
    if select_choice in ("1","2","3","4"):
         num1=float(input("enter your first number"))
         num2=float(input("enter the second number"))

         if select_choice=="1":
             print("you selected the addtion operation")
             result=num1+num2
             print(num1,"+",num2,"=",result)
         elif select_choice=="2":
             print("you selected the subraction operation")
             result=num1-num2
             print(num1,"-",num2,"=",result)
         elif select_choice=="3":
             print("you selected multiplication operation")
             result=num1*num2
             print(num1,"*",num2,"=",result)
         elif select_choice=="4":
             print("you selected the division operation")
             result=num1/num2
             print(num1,"/",num2,"=",result)
         next_caluclation=input("Do you want to continue (yes/no)")
         if next_caluclation=="yes":
             continue
         else:
             break
    else:
        print("you did not enter the valid option")
