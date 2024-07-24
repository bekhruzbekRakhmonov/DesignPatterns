import copy
from collections import OrderedDict

class Book:
    def __init__(self,name,authors,price, **rest):
        self.name = name
        self.authors = authors
        self.price = price
        self.__dict__.update(**rest)

    def __str__(self):
        mylist = []
        ordered = OrderedDict(sorted(self.__dict__.items()))
        
        for key in ordered.keys():
            mylist.append("{}: {}".format(key,ordered[key]))
            
            if key == "price":
                mylist.append("$")
            mylist.append("\n")

        return "".join(mylist)


class Prototype:
    def __init__(self):
        self.objects = {}

    def register(self,identifier,obj):
        self.objects[identifier] = obj

    def unregister(self,identifier):
        del self.objects[identifier]

    def clone(self,identifier,**attr):
        found = self.objects.get(identifier)

        if not found:
            raise ValueError(f"Incorrect object identifier: {identifier}")

        obj = copy.deepcopy(found)
        obj.__dict__.update(**attr)
        return obj

def main():
    book1 = Book("The C Programming Language", ("Brian W. Kernighan",
        "Dennis M. Ritchie"),price=118,publisher="Prentice Hall", length=228,
        publication_date="1978-02-22",tags=("C", "programming", "algorithms", 
        "data structures"))

    prototype = Prototype()
    cid = "k&r first"

    prototype.register(cid,book1)

    book2 = prototype.clone(cid,name="The C programming Language (ANSI)",
            price=48.99,length=274,publication_date="1988-04-01",edition=2)

    for i in (book1,book2):
        print(i)

    print("ID book1: {}, ID book2 {}".format(id(book1),id(book2)))

if __name__ == "__main__":
    main()
