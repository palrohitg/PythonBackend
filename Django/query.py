'''
    Three Model;
    1. Publishers
    2. Book 
    3. Store

    Questions:
    1. Insert 5 publishers 
    2. Insert 100 Books each publishers has 20 books
    3. 10 store 10 Books at each store 

1. bulk_create() --> list of 5 objects in publishers and create in one single query. 
2. Iterate all the Publishers : for each publishers objects: 
    Pub.objects.all():
        for i in range(20):
            books.append(Book(name = f"book{counters}", price=random.randint(50, 300) pubisher=publishers))

    Book.objects.bulk_create(books) // 100 records at onces.
    
'''
# https://betterprogramming.pub/django-select-related-and-prefetch-related-f23043fd635d

class Command():

    def handle(self, *args, **kwargs):
        pass