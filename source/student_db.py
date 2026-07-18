class StudentDB:

    def __init__(self):
        self.students = []

    def add_student(self, name):
        self.students.append(name)

    def remove_student(self, name):
        self.students.remove(name)

    def total_students(self):
        return len(self.students)

    def get_students(self):
        return self.students
    
db = StudentDB()
db.add_student("Alice")
db.add_student("Bob")
db.add_student("Charlie")

print(db.get_students())  #['Alice', 'Bob', 'Charlie']
print(db.total_students()) #3

db.remove_student("Bob") 

print(db.get_students())  #['Alice', 'Charlie']
print(db.total_students()) #2