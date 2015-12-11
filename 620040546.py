def get_isbn(book):
    return book[0]

def get_title(book):
    return book[1]

def get_author(book):
    return book[2]

def get_genre(book):
    return book[3]


def get_year(book):
    return book[4]

def get_qty(book):
    return book[5]

def get_salesprice(book):
    return book[6]

def co_authors(book):
    if len(get_author(book))<2:
        return []
    else:
        return get_author(book)[1:]

def check_price(bookshop,isbn):
    for i in range(0,len(bookshop[1])):
        if isbn in bookshop[1][i]:
            return bookshop[1][i][6]
    return 'Book not found'

def books_to_reorder(bookshop,qty):
    orderlist=[]
    for i in range(0,len(bookshop[1])):
        if bookshop[1][i][5]<qty:
            orderlist+=[(bookshop[1][i][0],bookshop[1][i][1])]
    return orderlist

def makebook(isbn,title,authors,genre,year,qtystck,saleprice):
    """constructor - creates a book"""
    return [isbn,title,authors,genre,year,qtystck,saleprice]

def bookshop():
    """constructor- creates a new bookshop"""
    return ("bookshop",[])

def add_book(book,bookshop):
    """constructor - adds a book tot eh bookshop"""
    return bookshop[1].append(book)
     
# example books
b1=["9780262510875","Struc. & Interp of Comp. Prog.",["Abelson H.","Sussman G.","Sussman J."],"CS text", 1996,12, 7340.00]
b2=["0216874068000","Algebra & No. Sys",["Hunter, J."],"Math text", 1985,30,1040.00]
b3=["9780521644082","Haskell School of Expr.",["Hudak, P."],"CS text", 2000,1,3455.00]

# code to create a uwi_bookshop
uwi_bookshop=bookshop()
add_book(b1,uwi_bookshop)
add_book(b2,uwi_bookshop)
add_book(b3,uwi_bookshop)
