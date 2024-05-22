book_list = ["1984", "To Kill a Mockingbird", "The Cabin at the End of the World"]
author_set = ["George Orwell", "Harper Lee", "Paul Tremblay"]
books_dict = {1: {"title": "1984" , "author" : "george orwell"}, 2: {"title": "To Kill a Mockingbird", "author": "Harper Lee"}, 3: {"title": "The Cabin at the End of the World", "author": "Paul Tremblay"}}

search_title = input("Enter Title:")
if search_title in book_list :
    print(f"Book Avialable! Author:{books_dict[book_list.index(search_title)+1]['author']}")
else: 
    print("Book Not Avilable")

print("All Books:")
for book in book_list:
    print(book)    

remove_book = input("Enter the title of the book to be removed or skip:")
if remove_book in book_list:
    remove_author = books_dict[book_list.index(remove_book)+1]['author']
    book_list.remove(remove_book)
    author_set.remove(remove_author) 
    del books_dict[book_list.index(remove_book)+1]
    print("Book removed successfully")
    print("Books available:", book_list) 

else: 
   print("book not found")
