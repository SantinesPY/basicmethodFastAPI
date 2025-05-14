#Code to initialize the uvicorn: 
# D:\FastAPI\FastAPI--proyect>
# uvicorn books:app --reload

from fastapi import Body, FastAPI

app = FastAPI()


BOOKS = [
    {'title' : 'title_one', 'author' : 'Author one','category':'science'},
    {'title' : 'title_two', 'author' : 'Author two','category':'math'},
    {'title' : 'title_three', 'author' : 'Author three','category':'spanish'},
    {'title' : 'title_four', 'author' : 'Author four','category':'science'},
    {'title' : 'title_five', 'author' : 'Author five','category':'science'},
    {'title' : 'title_six', 'author' : 'Author two','category':'science'},
]

# Method to take all the books
@app.get("/books")
async def read_all_books():
    return BOOKS

# Method to read the books depending the title
@app.get("/books/{book_title}")
async def read_book(book_title : str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

# Method to read the books usaing a category
@app.get("/books/")
async def read_category_by_query(category :str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

# Method to read the books using the author
@app.get("/books/{books_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return

# Method to create a new book
@app.post("/books/create_books")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

# Method to update a book
@app.put("/books/update_book")
async def update_book(updated_book=Body()):
     for i in range(len(BOOKS)):
         if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
             BOOKS[i] = updated_book

# Method to delete a book
@app.delete("/books/delete_books/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            BOOKS.pop(i)
            break

'''
Get all books from a specific author using path or query parameter

'''

@app.get("/books/byauthor/{author}")
async def read_books_by_author_path(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)

    return books_to_return