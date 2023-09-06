if __name__ == '__main__':
    n = int(input("Enter number of Students records: "))
    students_marks = {}
    for _ in range(n):
        name, *line = input("Enter Student Data: ").split()
        scores = list(map(float, line))
        students_marks[name] = scores
    query_name = input("Enter Student Name to Query: ")

    # print("Dictionary :- ", students_marks)
    # print("Query :- ", query_name)
    print("Student Name :- ", students_marks.get(query_name))
    marks = students_marks.get(query_name)
    # total_count = len(marks)
    total = 0.0
    # print("Total Students Marks Count : ", total_count)

    # If we use Line#24, below for loop is not required as sum() is iterable over result
    # for i in marks:
    #     total = total + i
    #     print(total)

    # print("Average is : ", "{:.2f}".format(total/len(marks)))
    print("Average is : ", "{:.2f}".format(sum(marks) / len(marks)))
