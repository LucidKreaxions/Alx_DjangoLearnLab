### Create Operation

Command:
```python
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

### Retrieve Operation

Command:
```python
books = Book.objects.all()
for b in books:
    print(b.title, b.author, b.publication_year)


### Update Operation

Command:
```python
book.title = "Nineteen Eighty-Four"
book.save()

### Delete Operation

Command:
```python
book.delete()
books = Book.objects.all()
print(books)
