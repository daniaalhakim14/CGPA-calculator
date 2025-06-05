# Author: Danial Hakim Bin Norasmadi
# Date: 22/02/2024
# Program: CGPA Calculator
# Language: Python

# import module/library
import os
import sys

# global variable declaration
space = "\t\t\t\t"
totalSem = 0
# to count the number of semesters
counter = 1
p = 1

def main():
    # declare as global variables to modify within the function
    global totalSem, counter

    print("\n" + space + "CGPA Calculator \n")

    # validation
    # if the user enters 0 or a negative value, the system will not crash and ask the user to enter the correct value
    if totalSem == 0:
        while True:
            totalSem_input = input(space + "Enter the number of semesters you are taking: ")
            if totalSem_input.isdigit():
                totalSem_integer = int(totalSem_input)
                if totalSem_integer > 0:
                    totalSem = totalSem_integer
                    break
                else:
                    print(space + "Number of semesters taken must be larger than 0.")
                    input(space + "Please enter to continue...\n")
            else:
                print(space + "Please enter a valid positive integer for the number of semesters taken.")
                input(space + "Please enter to continue...\n")

    # initialize semesterGPA
    semesterGPA = [0.00] * totalSem

    # while loop
    while True:
        os.system("cls")
        print("\n" + space + "CGPA Calculator \n")
        print(space + "1 - Calculate GPA")
        print(space + "2 - Calculate CGPA")
        print(space + "3 - Display current GPA")
        print(space + "4 - Search semester")
        print(space + "5 - Sort semester in order highest GPA")
        print(space + "6 - Sort semester in order lowest GPA")
        print(space + "7 - Exit\n")
        option = int(input(space + "Choose an option: "))

        if option == 1:
            CalculateGPA(semesterGPA, totalSem)
        elif option == 2:
            CalculateCGPA(semesterGPA, totalSem)
        elif option == 3:
            displayGPA(semesterGPA, totalSem)
        elif option == 4:
            searchSemester(semesterGPA, totalSem)
        elif option == 5:
            sortSemesterASC(semesterGPA, totalSem)
        elif option == 6:
            sortSemesterDESC(semesterGPA, totalSem)
        elif option == 7:
            print(space + "Program Terminated")
            break
        else:
            print(space + "Please choose between options 1 - 7")
            input(space + "Press Enter to continue...")

def CalculateGPA(semesterGPA, totalSem):
    # declare as global to modify within the function
    global counter, p

    #can only use in IDE
    os.system("cls")
    print("\n" + space + "Calculate GPA\n")
    print(space + "Semester: " + str(counter))

    # validation
    # if the user enters 0 or a negative value, the system will not crash and ask the user to enter the correct value
    while True:
        noOfSubject_input = input(space + "Enter the number of subjects taken: ")
        if noOfSubject_input.isdigit():
            noOfSubject_integer = int(noOfSubject_input)
            if noOfSubject_integer > 0:
                noOfSubject = noOfSubject_integer
                break
            else:
                print(space + "Number of subjects taken must be larger than 0.")
                input(space + "Please enter to continue...\n")
        else:
            print(space + "Please enter a valid positive integer for the number of subjects taken.")
            input(space + "Please enter to continue...\n")

    credit = [0] * noOfSubject
    point = [0.00] * noOfSubject
    grade = [" "] * noOfSubject

    print("\n" + space + "-----------------------------------\n")

    # i = 0, normally compute count starts with zero
    # eg. for i in range(10):
    # print(i)
    # output will be 0-9
    #
    # validation
    # if the user enters 0 or a negative value, the system will not crash and ask the user to enter the correct value
    for i in range(noOfSubject):
        while True:
            credit_input = input(space + "Enter the credit hour for the subject: ")
            if credit_input.isdigit():
                credit_integer = int(credit_input)
                if credit_integer > 0:
                    credit[i] = credit_integer
                    break
                else:
                    print(space + "Credit hour must be larger than 0.")
                    input(space + "Please enter to continue...\n")
            else:
                print(space + "Please enter a valid positive integer for the credit hour.")
                input(space + "Please enter to continue...\n")

        while True:
            grade[i] = input("\n" + space + f"Enter the grade for subject {i + 1}: ")
            if grade[i] in ["A+", "a+", "A", "a", "A-", "a-", "B+", "b+", "B", "b", "B-", "b-", "C+", "c+",
                             "C", "c", "C-", "c-", "D+", "d+", "D", "d", "F", "f", "DH", "MH", "TH", "TL", "PK"]:
                print("\n" + space + "-----------------------------------\n")
                break
            else:
                print(space + "Please enter a valid grade.")
                input(space + "Please enter to continue...\n")

    # can use either 3 methods
    # if grade[j] == "A+" or grade[j] == "A":
    # point[j] = 4.00
    # or
    # if grade[j].upper() == "A+":
    # point[j] = 4.00
    # elif grade[j].upper() == "A":
    # point[j] = 4.00
    #

    for j in range(noOfSubject):
        if grade[j] in ["A+", "a+", "A", "a"]:
            point[j] = 4.00
        elif grade[j] in ["A-", "a-"]:
            point[j] = 3.67
        elif grade[j] in ["B+", "b+"]:
            point[j] = 3.33
        elif grade[j] in ["B", "b"]:
            point[j] = 3.00
        elif grade[j] in ["B-", "b-"]:
            point[j] = 2.67
        elif grade[j] in ["C+", "c+"]:
            point[j] = 2.33
        elif grade[j] in ["C", "c"]:
            point[j] = 2.00
        elif grade[j] in ["C-", "c-"]:
            point[j] = 1.67
        elif grade[j] in ["D+", "d+"]:
            point[j] = 1.33
        elif grade[j] in ["D", "d"]:
            point[j] = 1.00
        else:
            point[j] = 0.00

    sum = 0
    total = 0

    # calculate total points for each subject
    for i in range(noOfSubject):
        total = credit[i] * point[i]
        sum += total

    totalCredit = 0

    # calculate total credit
    for i in range(noOfSubject):
        totalCredit += credit[i]

    # calculate GPA for the semester
    gpa = sum / totalCredit

    print("\n\n" + space + "Total Points: " + str(round(sum, 2)) + " Total Credit Hours: " +
          str(round(totalCredit, 2)) + " GPA: " + str(round(gpa, 2)))

    # array/list index always start at 0
    # counter = 1
    # semester[1-1] = gpa
    semesterGPA[counter - 1] = gpa

    # increment by 1 to get the next semester
    counter += 1

    if p < totalSem:
        option = input(space + "Do you want to enter GPA for semester " + str(counter) + " ? (Y/N): ")
        p += 1
        if option == 'Y' or option == 'y':
            CalculateGPA(semesterGPA, totalSem)
        else:
            input(space + "Press enter to continue...")
    else:
            input(space + "Press enter to continue...")

def CalculateCGPA(semesterGPA, totalSem):
    os.system("cls")
    print("\n" + space + " Calculator CGPA\n")

    # validation if the user doesn't enter GPA for at least 1 semester
    if semesterGPA[0] == 0:
        print(space + "Please enter GPA for at least 1 semester")
        input(space + "Press Enter to continue...")
        main()

    CGPA = sum(semesterGPA) / totalSem
    print(space + "CGPA: " + str(round(CGPA, 2)))
    input(space + "Press enter to continue...")

def displayGPA(semesterGPA, totalSem):
    os.system("cls")
    print("\n" + space + "GPA for every semester\n\n")
    for i in range(totalSem):
        print(space + "Semester " + str(i + 1) + ": " + str(round(semesterGPA[i], 2)))
    input(space + "Press enter to continue...")

def searchSemester(semesterGPA, totalSem):
    os.system("cls")

    found = False

    print("\n" + space + "Search Semester\n\n")
    sem = input(space + "Enter semester: ")

    for i in range(totalSem):
        if (i + 1) == int(sem):
            print(f"\n{space}Semester {i + 1} : {semesterGPA[i]:.2f}")
            found = True
            input(space + "Press enter to continue...")
            break

    if not found:
        print("\n" + space + "Semester " + str(sem) + " not found.")
        input(space + "Press enter to continue...")


def sortSemesterASC(semesterGPA, totalSem):
    os.system("cls")

    # Sort in ascending order
    # Iterate over each element of the list
    for i in range(totalSem):
        # Assume the current index has the minimum value
        min_position = i

        # Check the rest of the elements for a smaller value
        for j in range(i + 1, totalSem):
            if semesterGPA[j] < semesterGPA[min_position]:
                min_position = j

        # Swap the current element with the minimum found
        semesterGPA[i], semesterGPA[min_position] = semesterGPA[min_position], semesterGPA[i]



    print("\n" + space + "GPA for every semester from highest to lowest\n")
    # Print the sorted list
    for i in range(totalSem):
        print(space + f"Semester {i + 1} : {semesterGPA[i]:.2f}")
    input("\n"+ space + "Press enter to continue...")

def sortSemesterDESC(semesterGPA, totalSem):
    os.system("cls")

    # Sort in descending order
    # Iterate over each element of the list
    for i in range(totalSem):
        # Assume the current index has the maximum value
        max_position = i

        # Check the rest of the elements for a larger value
        for j in range(i + 1, totalSem):
            if semesterGPA[j] > semesterGPA[max_position]:
                max_position = j

        # Swap the current element with the maximum found
        semesterGPA[i], semesterGPA[max_position] = semesterGPA[max_position], semesterGPA[i]

    print("\n" + space + "GPA for every semester from lowest to highest\n")
    # Print the sorted list
    for i in range(totalSem):
        print(space + f"Semester {i + 1} : {semesterGPA[i]:.2f}")
    input("\n"+ space + "Press enter to continue...")

# call the main function
main()


