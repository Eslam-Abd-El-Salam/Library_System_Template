#!/usr/bin/env python
# coding: utf-8

# ![image.png](attachment:image.png)

# > ### Harry works in the library, Harry is tired of writing data in paper records so Harry decides to go digital.
# > ### Harry wants a program to do all the operations in the library.
# > ### Let's help Harry!

# # Task 1 : 
# - #### task 1.1 Make Class(Library) with attributes:
#     - booksList  
#     - name of library  
#     - lended books (name of user, book) 
# - #### task 1.2 Make method to display available Books.
# - #### task 1.3 Make method for books lending.
#     - Don't forget to check if book isn't already lended 
# - #### task 1.4 Make method to add Book to library.
# - #### task 1.5 Make method to return borrowed book.

# In[1]:


class Library:
    
    #attributes
    def __init__(self ,  booksList , name):
        
        self.booksList    = list(map(lambda x: x.capitalize(), booksList))
        self.name         = name
        self.lended_books = {}
        
    #methods
    
    def display_books(self):
        
        
        if len(self.booksList) == 0 :
            print("No Books Added Yet..")
        else:
            print(f"All Available books of {self.name} Library: ")
            print("============================================")
            for book in (self.booksList):
                print(book)
    
    def book_lend(self, user_name, book_name):
        
        if type(user_name) == str and type(book_name) == str:
            
            if user_name.capitalize() in (self.lended_books.keys()):
                print("Sorry this user is taken Chose anotther one..")
                
            elif book_name.capitalize() in (self.lended_books.values()):
                
                print("Sorry book is already lended..")
                
            elif book_name.capitalize() in self.booksList:
                
                self.lended_books[user_name.capitalize()] = book_name.capitalize()
                self.booksList.remove(book_name.capitalize())
                print(f"Book Already Found and User Name: '{user_name}' recorded. Happy Reading ^_^")
                
                
            else:
                
                print(f"Sorry {book_name.capitalize()} book not Available in {self.name} Library.")
                
        else:
            
            print("please enter valid names")
    
    def add_book(self, book_name ):
        
        if type(book_name) == str:
            
            if  book_name.capitalize() not in self.booksList:
                self.booksList.append(book_name.capitalize())
                print("Book Added Successfuly.")
                
            else:
                
                print(f"book {book_name} Alredy Found.")
        else:
            
            print("Please Enter valid book name")
    
    def return_borrowed_book(self,user_name , book_name):
        
        if type(user_name) == str and type(book_name) == str:
            
            if user_name.capitalize() in (self.lended_books.keys()):
                if self.lended_books[user_name.capitalize()] == book_name.capitalize():
                    del self.lended_books[user_name.capitalize()]
                    self.add_book(book_name)
                    
                else:
                    print("Sorry name of book not related to this user.")    
            else:
                
                print(f"Sorry {user_name} not Available in Records.")
                
        else:
            
            print("please enter valid names")
        


# # Task 2 : 
# - #### task 2.1 Make object(Harry) with attributes:
#     - booksList  = ['Python', 'Rich Daddy Poor Daddy', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS']
#     - name of lirary  = "CodeWithHarry"
# - #### task 2.2 Make program run with this choices. __(Don't forget the welcome message)__
#     - 1. Display Books
#     - 2. Lend a Book
#     - 3. Add a Book
#     - 4. Return a Book
# - #### task 2.3 Make prgram ends or continue.

# In[3]:


booksList = ['Python', 'Rich Daddy Poor Daddy', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS']
name_of_lirary = "CodeWithHarry"

Harry = Library(booksList,name_of_lirary)
current_object = Harry

def take_user_input():
    global flag
    flag = 0
    while True:
        print("===================================================================")
        print("Welcome to our Library, please type a number from the next options:")
        print("1) Display Books")
        print("2) Lend a Book")
        print("3) Add a Book")
        print("4) Return a Book")
        print("5) To Exit")
        try:
                user_choice = int(input(''))
                
        except ValueError:
            
                print("please enter valid number!")
                continue
            
        if   user_choice == 1:
            
            current_object.display_books()
            
        elif user_choice == 2:
            
            user_name = input("user_name: ")
            book_name = input("book name: ")
            current_object.book_lend(user_name, book_name)
            
        elif user_choice == 3:
            
            book_name = input("book name: ")
            current_object.add_book(book_name)
            
        elif user_choice == 4:
            user_name = input("user_name: ")
            book_name = input("book name: ")
            current_object.return_borrowed_book(user_name,book_name)
        elif user_choice == 5:
            flag = 1
            break
        else:
            print("plese enter valid num from 1 to 5")
            continue


while True:
    take_user_input()
    if flag == 1:
        print("Goodbye, have a nice day")
        break
    
    


# In[ ]:




