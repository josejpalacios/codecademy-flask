# TableName.query.all(): Get all entries from a model called TableName
# TableName.query.get(ID): Get entry with a primary key value of ID from model TableName

# Store result of .get() to a variable to get access to attributes of result.

# =============
# playground.py
# =============
from app import db, Book, Reader, Review, Annotation

#query all the readers from the Reader model
readers = Reader.query.all()
print(readers)

#get an entry with id = 123 
reader = Reader.query.get(123)
print(reader)

#reader with id = 450
reader = Reader.query.get(450)
print("Reader with id = ", reader.id, "is called", reader.name)

#Loop through all the readers and print their e-mails
print("\nPrint all the readers in a loop:")
for reader in readers:
  print(reader.email)

#or inline
#[print(reader.email) for reader in readers]

print("\nCheckpoint1: fetching all the reviews")
reviews = Review.query.all()

print("\nCheckpoint2: looping through all the reviews and printing their text")
#your loop line 1
#you loop line 2
for review in reviews:
  print(review.text)

print("\nCheckpoint3: fetching a book with id = 13 using the get() function")
book_1 = Book.query.get(12)
