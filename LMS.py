import os
from datetime import date

class library:
    def __init__(self,list,name):
        self.Libname=name
        file = open('stock.txt','a+')
        for books in list:
            file.write(books+'\n')
        file.close()

    def displayBooks(self):
        file = open('stock.txt','r')
        stock=file.read().split('\n')
        for books in stock:
            print(books)
        file.close
    def lendBook(self,user,book):
        file = open('records.txt','r')
        f = open('records.txt','a+')
        file2 = open('stock.txt','r')
        stock = file2.read().split('\n')
        records = file.read().split('\n')
        if book in stock:
            if book not in records:
                f.write('\n'+book+'\n'+f'lend by {user}'+' at '+f"{date.today()}")
                print("Lender-Book database has been updated. You can take the book now")
                print(f"{book} is lended by {user} at {date.today()}")
                print("Kindly return within 15 days.")
            else:
                print("Book is lended by someone")
        else:
            print("Book is not available in stock")
        file.close()
        f.close()
        file2.close()

    def returnBook(self,book):
        file = open('records.txt','r')
        r = file.readlines()
        for i in range(len(r)):
            if book ==  r[i].split('\n')[0]:
                r[i] = f"{book} returned at {date.today()} \n"
                with open("records.txt", "w") as f:
                    f.writelines(r)
                print("Thanks for returning the book")
        file.close()

    def addBook(self,book):
        file = open('stock.txt', 'a+')
        file.write('\n'+book)
        file.close()
        print("Book successfully added.")
if __name__== '__main__':
    Sam = library([],"CodeWithHarry")
    print("\t\t\t\tWelocome To Sam Library\t\t")
    print("===============================================================================")
    user_choice = 1;
    while(user_choice!=5):
        print("Enter The choice to continue")
        print("1.Display Books")
        print("2.Lend Book")
        print("3.Add a book")
        print("4.Return a Book")
        print("5.Exit")
        user_choice = int(input())
        if user_choice not in [1,2,3,4,5]:
            print("Please input the valid option")
            continue

        if user_choice == 1:
            Sam.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your name:")
            Sam.lendBook(user,book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:")
            Sam.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")
            Sam.returnBook(book)

        elif user_choice == 5:
            print("Thanks for visiting our library")