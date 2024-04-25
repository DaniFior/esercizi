student : dict = {"Math":input("Insert your vote in MATH /100: "), "History":input("Insert your vote in HISTORY /100: "), "Sport":input("Insert your vote in SPORT /100: ")}
def exam(student) :
    somma = []
    for a,b_input in student.items():
        b = int(b_input)
        somma.append(b)
    print(student)
    total = sum(somma)
    average = total / len(somma)
    if average >= 60.0 :
        print("The student has passed the exam with a average of {}".format(average))
    elif average < 60.0:
        print("The student has not passed the exam because his average is: {}".format(average))

exam(student)
