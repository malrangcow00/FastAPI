from fastapi import Body, FastAPI

app = FastAPI()


Books_list = [
    {'title': 'FastAPI', 'author': 'MalrangCow', 'category': 'IT'},
    {'title': 'How to hack WhiteHouse', 'author': 'Unknown', 'category': 'IT'},
    {'title': "MalrangCow's Life", 'author': 'MalrangCow', 'category': 'biography'},
    {'title': 'The Mathematics of Tuna', 'author': 'ChubbyCat', 'category': 'math'},
    {'title': 'One One and Two', 'author': 'Kazuya Mishima', 'category': 'math'},
    {'title': 'Dune', 'author': 'Frank Patrick Herbert', 'category': 'SF'},
    {'title': 'What Should We Do', 'author': 'MalrangCow', 'category': 'Philosophy'}
]


@app.get("/books-list")
async def read_books_list():
    return Books_list

# Path parameter
# @app.get("/baseurl/{dynamic_path_parameter}")
# async def function_name(dynamic_path_parameter: type):
#     function...
#         return result

@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in Books_list:
        if book.get('title').casefold() == book_title.casefold():
            return book

# Query parameter
# @app.get("/baseurl/")
# async def function_name(query_parameter: type):
#     function...
#         return result

# add default value None
@app.get("/books")
async def get_book_by_author(author: str = None):
    # if author == None:
    if author == None:
        return Books_list
    books = []
    for book in Books_list:
        if book.get('author').casefold() == author.casefold():
            books.append(book)
    return books

@app.get("/books/{book_author}/")
async def get_bookg_by_author_path_category_query(book_author: str, category: str):
    books = []
    for book in Books_list:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books.append(book)
    return books

@app.get("/books/find")
async def get_book_by_query(author: str = None, category: str = None):
    books = []
    for book in Books_list:
        if book.get('author').casefold() == author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books.append(book)
    return books

# 2개 이상의 쿼리 추가시 &로 연결
@app.get("/find-book")
async def get_book_by_query(author: str = None, category: str = None):
    books = []
    if author is None and category is None:
        return Books_list
    elif author is not None and category is not None:
        for book in Books_list:
            if book.get('author').casefold() == author.casefold() and \
                    book.get('category').casefold() == category.casefold():
                books.append(book)
    elif author is not None:
        for book in Books_list:
            if book.get('author').casefold() == author.casefold():
                books.append(book)
    elif category is not None:
        for book in Books_list:
            if book.get('category').casefold() == category.casefold():
                books.append(book)
    else:
        return {"error": "Invalid query"}
    return books


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    Books_list.append(new_book)


@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(Books_list)):
        if Books_list[i].get('title').casefold() == updated_book.get('title').casefold():
            Books_list[i] = updated_book


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(Books_list)):
        if Books_list[i].get('title').casefold() == book_title.casefold():
            Books_list.pop(i)
            break
