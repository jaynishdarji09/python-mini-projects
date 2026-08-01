class Student:
    def __init__(self, roll, name):
        self.roll = roll
        self.name = name

class Marks(Student):
    def __init__(self, roll, name, m1, m2, m3):
        super().__init__(roll, name)
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def total(self):
        return self.m1 + self.m2 + self.m3
    def percentage(self):
        return self.total() / 3

students = []
while True:
     print("1.Add Students")
     print("2.Display students")
     print("3.save to file")
     print("4.exit")

     choice = int(input("enter choice : "))

     if choice == 1:
         roll = input("enter roll no : ")
         name = input("enter nname : ")
         m1 = int(input("enter student 1 marks : "))
         m2 = int(input("enter student 2 marks : "))
         m3 = int(input("enter student 3 marks : "))

         s = Marks(roll, name, m1, m2, m3) 
         students.append(s)
         print("student added successfullly")

     elif choice == 2:
         if len(students) == 0:
             print("no records found")
         else:
             print("\n Roll \t Name \t total \t Percentage")

             for s in students:
                 print(f"{s.roll}\t{s.name}\t{s.total()}\t{s.percentage():.2f}%")

     elif choice == 3:
         file = open("student.txt", "w")

         for s in students:
             file.write(f"{s.roll},{s.name}, {s.total()}, {s.percentage():.2f}\n")
             file.close()
             print("data written successfullly")

     elif choice == 4:
        print("thank you!")
        break

     else:
         print("invalid choice")
         
         
                 

         
         


    
        