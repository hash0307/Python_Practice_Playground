if __name__ == '__main__':
    grades = []
    for _ in range(int(input("Enter Total Students: "))):
        name = input("Enter Student Name: ")
        score = float(input("Enter Score: "))
        tempList = [name,score]

        grades.append(tempList)

    print("Students Grades are :- ", grades)

    second_highscore = sorted(list(set(marks for name,marks in grades)))[1]
    print("Second Highscore: ", second_highscore)

    students = sorted(list(name for name, marks in grades if marks == second_highscore))
    print("Students with second highest score: ", students)

    for student_name in students:
        print(student_name)