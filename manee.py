#Print First 10 Natural numbers using with "While loop"

#i=1
#while i<=10:
#    print(i)
#    i+=1
    
#Display numbers from -10 to -1 using for loop


#for x in range(-10,-1):
#    print(x)

#Write a program to print multiplication table of a given number

#n=int(input("enter the number:"))
#for i in range(1,21):
#    print(n,"*",i,"=",n*i)

#Display numbers from a list using loop
#l1=[10,20,30,40,50,60,70,80,90,100]
#for num in l1:
#    print(num)

#Calculate the sum of all numbers from 1 to a given number

#num=int(input("Enter the number:"))
#sum=0
#for i in range(1,num+1):
#    sum=sum+i
#    i=i+1
#print("sum = ",sum)

    

#Print list in reverse order using a loop

#list1=[10,20,30,40,50]
#size=len(list1)-1
#for i in range(size,-1,-1):
#    print(list1[i])


#Use else block to display a message "Done" after successfull execution of for loop

#count=0
#for count in range(10):
#    print("Hello Maneesha",count)
#else:
#    print("end of for loop")    
#print("Good bye!")

#Count the total number of digits in a number 

#num=int(input("Enter a number:"))    
#count=0
#while(num>0):
#    num=num//10
#    count=count+1
#print("Total Count = ", count)    
    

    
    
    
    
#Write a program to display all prime numbers within a range

#starter=int(input("Enter the starter interval:"))
#ender=int(input("Enter the ender interval:"))
#for num in range(starter,ender+1):
#    if num>1:
#        for i in range(2,num):
#            if(num%i)==0:
#                break
#        else:
#                print(num)
        
    

#Fibonacci Series:
#a=0
#b=1
#for i in range(10):
#    c=a+b
#    a=b
#    b=c
#    print(c)
    
#n1=0
#n2=1
#for i in range(10):
#    n3=n1+n2
#    n1=n2
#    n2=n3
#    print(n3,end=" ")    

#GUI = Graphical User Interface
 
from tkinter import*
root=Tk()
root.geometry("500x300")

def getvals():
    print("Accepted")
    
#Heading
Label(root, text="Python Registration Form", font="ar 15 bold").grid(row=0, column=3)

#Field Name
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency")
paymentmood= Label(root, text="Payment Mood")

#Packing Fields
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmood.grid(row=5, column=2)

#Variable for storing data
namevalue= StringVar
phonevalue= StringVar
gendervalue= StringVar
emergencyvalue= StringVar
paymentmoodvalue= StringVar
checkvalue= IntVar

#Creating entry field
nameentry= Entry(root, textvariable_=namevalue)
phoneentry= Entry(root, textvariable_=phonevalue)
genderentry= Entry(root, textvariable_=gendervalue)
paymentmoodentry= Entry(root, textvariable_=paymentmoodvalue)
emergencyentry= Entry(root, textvariable_=emergencyvalue)

#Packing entry field
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmoodentry.grid(row=5, column=3)

#Creating Checkbox

checkbtn = Checkbutton(text="remember me?", variable=checkvalue)
checkbtn.grid(row=6, column=3)

#Submit Button
Button(text="Submit", command=getvals).grid(row=7, column=3)
root.mainloop()
