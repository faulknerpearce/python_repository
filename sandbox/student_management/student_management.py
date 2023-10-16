class Student:
  # Create a constructor for the student class. 
  def __init__(self, name, year):
    self.name = name 
    self.year = year
    self.grades = []
    self.attendance = {}
  
  # Add a constructor to print the instance of the created object. 
  def __repr__(self):
    return f"This student's name is: {self.name}, and is in year: {self.year}"
  
  # This method will add a grade to the student's grades list. 
  def add_grade(self, grade):
    # Only add the grade to the student's grades if the grade is of type Grade.
    if type(grade) is Grade:
      self.grades.append(grade)
  
  # This method will mark the student's attendance for a specific class on a given day.
  def mark_attendance(self, class_name, day, attended):
     if self.attendance.get(class_name, 0):
        self.attendance[class_name].update({day: attended})
     else:
        self.attendance.update({class_name: {day: attended}})
  
  # This method will calculate the total score of the student's grades, 
  def calculate_grades_total(self):
     return sum(self.grades)

class Grade:
  # Create a constructor for the grade class. 
  def __init__(self, score):
    self.score = score
    self.minimum_passing = 65
  
  # This method will check if the student's grade is above or below the minimum passing score. 
  def is_passing(self, student_grade):
    if type(student_grade) is Grade:
      if student_grade.score >= self.minimum_passing:
        print(f"You passed with a score of {student_grade.score}.")
        return True
      else:
        print(f"Your grade did not reach the minimum passing score of {self.minimum_passing}. Your score was {student_grade.score}")
        return False

# This function gets the current day of the week as a string (e.g., "Monday").
def get_day():
   from datetime import datetime
   weekday_strings = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
   
   current_time = datetime.now()
   day = current_time.weekday()
   
   return weekday_strings[day]

# Create an instance of the student. 
roger = Student("Roger van der Weyden", 10)

# Create grade objects from the Grade class. 
computer_science = Grade(66)
math = Grade(75)
chemistry = Grade(90)

# Add the grades to the student's grade list. 
roger.add_grade(computer_science)
roger.add_grade(math)
roger.add_grade(chemistry)

# Print if the student passed the class. 
computer_science.is_passing(roger.grades[0])

# Update the student's attendance record. 
roger.mark_attendance("Computer Science", get_day(), True)
