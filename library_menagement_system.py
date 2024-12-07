class Library:
    def __init__(self):
        self.file=open("books.txt","a+",encoding="utf-8")
        
    def __del__(self):
        print("Destructor")
        self.file.close()

    def list_book(self):
        self.file.seek(0)
        for line in self.file:
            line_lst=line.split(",")
            if len(line_lst)==1:    #Boş satır varsa bu satırı atla
                continue
            print("Book title:"+ line_lst[0]+", Author name: "+line_lst[1])


    
    def add_book(self):
        title=input("Enter the title of the book:")
        author=input("Enter the name of the author:")
        year=input("Enter the first release year:")
        pages=input("Enter the number of pages:")
        self.file.write(title+","+author+","+year+","+pages+"\n")
        print(f"The book named {title} has been added to the file.")
        
        
        
    def remove_book(self):
        lst_lines=[]
        title=input("Enter the title of the book you want to remove:")
        self.file.seek(0)
        for line in self.file:
            line_lst=line.split(",")
            if len(line_lst)==1:    #Boş satır varsa bu satırı atla
                continue
            if title in line_lst:
                continue
            lst_lines.append(line)
        self.file.truncate(0)
        for line in lst_lines:
                self.file.write(str(line) + "\n")
        print(f"The book named {title} has been removed from the file.")
        
       
        
try:
    lib = Library()
    while True:
        choice=input("""
        *** MENU***
        1) List Books
        2) Add Book
        3) Remove Book
        4) Quit
                     """)
        if choice == "1":
            lib.list_book()
        elif choice == "2":
            lib.add_book()
        elif choice == "3":
            lib.remove_book() 
        elif choice ==  "4":
            print("Exiting the program...")
            break
        else:
            print("Please enter 1, 2, 3 or 4")
finally:
    del lib
