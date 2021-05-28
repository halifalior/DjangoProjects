from django.shortcuts import render
from django_pandas.io import read_frame # this
from books.models import Book
from users.models import UserProfile
import pandas as pd

# There are 2 data sources
# books.csv -> a file of books details to be read to a pandas DataFrame
# Books -> model class that is saved in the db.sqlite3 database
# There are the following functions
# insert_row_to_df() - the function gets a dataframe and a row (list of book details) and append it to the dataframe
# insert_row_to_db() - the function gets a row (list of book details) and stores it in the books database
# df_to_db() - the function reads the books dataframe and add it rows to the Book table in the db.sqlite3
# db_to_def() - read all the books table from db.sqlite3 and return a dataframe of all the books details
# save_df_to_csv - save the updated dataframe to the csv file

def insert_row_to_df (df, row):
    insert_loc = df.index.max()

    if pd.isna(insert_loc):
        df.loc[0] = row
    else:
        row.insert(0,insert_loc+1)
        df.loc[insert_loc + 1] = row

def insert_row_to_db (row):
    newbook=Book()
    newbook.title=row[1]
    newbook.description=row[2]
    newbook.price=int(row[3])
    newbook.pages=int(row[4])
    newbook.image=row[5]
    newbook.genre=row[6]
    newbook.save()


def df_to_db():
    # read the books.csv to books dataframe

    books_df = pd.read_csv("C:\\projects\\myprojects\\books\\books.csv")

    # insert a new row to the books dataframe
    insert_row_to_df(books_df,['book99','description of book99',99,99,'img.9','CH'])
    print(books_df)

    # loop over the dataframe rows and add the rows to the Books table

    for i in range(0, len(books_df)):
        insert_row_to_db(books_df.iloc[i])

def db_to_df():
    #read all the books details from Books table in sqlite.db3
    books = Book.objects.all()
    #create a book dataframe
    books_df = read_frame(books)
    print(books_df)
    return(books_df)


def save_df_to_csv(books_df):
    books_df.to_csv("C:\\projects\\myprojects\\books\\books.csv",index=False)


def books_index(request):

    books_df=pd.DataFrame()
    books_df = db_to_df()
    print("***********************************************************")
    print(books_df)
    save_df_to_csv(books_df)

    df_to_db()

    books = Book.objects.all()
    if (request.user.is_authenticated):
        if request.user.userprofile.age < 18 :
            books= Book.objects.filter(genre='CH')
    context = {
        'books': books
    }

    return render(request, 'books_index.html', context)

# this function gets a bookid and display its full details

def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        'book': book
    }
    return render(request, 'book_detail.html', context)