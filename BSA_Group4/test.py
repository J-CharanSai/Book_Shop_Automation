from Class import Customer, Employee, Vendor, Publisher,Book, Owner, Manager,NotInCollection,Transaction,SalesClerk
from DataBaseClass import BookDB, PublisherDB, VendorDB, TransactionDB, NotInCollectionDB



print("Testing get book")
book_=BookDB().get_bookbyisbn(97881)
print(book_.get_booktitle(),book_)
book_=BookDB().get_bookbyisbn(1231145)
print(book_)


'''print("\nTesting add book")
book_1=Book("harrypotter","JKrowling",1000,12345,10,17,0,5,12)
BookDB().add_book(book_1,10)'''

print("\nTesting get statistics")
print(TransactionDB().get_statistics("2021/04/14","2021/04/5"))
print(TransactionDB().get_statistics("2021/04/14","2021/04/15"))
'''
print("\nTesting add request")
req_=NotInCollection(1,None,"batman","bruce","wayne",56789)
NotInCollectionDB().add_request(req_)'''

print("\nTesting view request")
print(NotInCollectionDB().view_requests())

print("\nTesting search vendor")
print(VendorDB().search_vendorbyid(1))
