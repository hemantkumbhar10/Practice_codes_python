class Book:
    def __int__(self):
        self.title = None

my_fav = Book()
my_fav.title = 'Head First Programming'
your_fav = Book()
your_fav.title = 'Learn Python the hard way'
my_fav.title = 'Learning Python'
print('My favourite is', my_fav.title)
print('Yours is', your_fav.title)