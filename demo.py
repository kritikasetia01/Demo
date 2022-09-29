import pandas as pd

books_path="C://Users//This pc//BX-Books.csv"

#with open(books_path) as f:
#    print (f.readlines())

data = pd.read_csv(books_path)

