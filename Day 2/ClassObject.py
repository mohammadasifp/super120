class library:
    def __init__(self,id,name,author,year,publisher):
        self.id=id
        self.name=name
        self.author=author
        self.year=year
        self.publisher=publisher
    
    def display(self):
        print(f"Book ID: {self.id}")
        print(f"Book Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Year of Publication: {self.year}")
        print(f"Publisher: {self.publisher}")

book1=library(1,"Python Programming","John Smith",2020,"ABC Publications")
book1.display()
book2=library(2,"Data Structures and Algorithms","Jane Doe",2019,"XYZ Publications")
book2.display()

