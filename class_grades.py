# a simple program that calculates grades in a class using dictionaries, lists and functions.

lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

students = [lloyd, alice, tyler]

# Add your function below!
def average(numbers):
  total = sum(numbers)
  total = float(total)
  total = total / len(numbers)
  return total

def getAverage(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  test = average(student["tests"])
  return 0.1 * homework + 0.3 * quizzes + 0.6 * test

def letterGrade(score):
  if score >= 90:
    return "an A."
  elif score >= 80:
    return "a B."
  elif score >= 70:
    return "a C."
  elif score >= 60:
    return "a D."
  else :
    return "an F."

def classAverage(class_list):
  grades = []
  for student in class_list:
    grades.append(getAverage(student))
  return average(grades)

averages = [getAverage(students[0]), getAverage(students[1]), getAverage(students[2])]

print "%s receives %s" % (students[0]["name"], letterGrade(getAverage(students[0])))
print "%s receives %s" % (students[1]["name"], letterGrade(getAverage(students[1])))
print "%s receives %s" % (students[2]["name"], letterGrade(getAverage(students[2])))

print "The class average is %s" % classAverage(students)
print "The average letter grade is %s" % letterGrade(classAverage(students))
