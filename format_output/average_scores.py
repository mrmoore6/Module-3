"""
Program: average_scores.py
Author: Michael Moore
Last Date Modified: 9/12/20

This program takes 3 tests input and return and average of them.
"""
def average():
    score1 = int(input("Enter 1st Test Score: "))
    score2 = int(input("Enter 2nd Test Score: "))
    score3 = int(input("Enter 3rd Test Score: "))
    return (score1 + score2 + score3) / 3

if __name__ == '__main__':
    last_name = input("Enter Last Name: ")
    first_name = input("Enter First Name: ")
    age = int(input("Enter Age: "))
    average_scores = average()
    print(f"{last_name}, {first_name} age: {age}", "average grade: {:.2f}".format(average_scores))

#input 1 Moore,Michael,22,99,99,94 output 1 Moore, Michael age: 22 average grade: 97.33
#input 2 Moore,Michael,22,87,56,34 output 2 Moore, Michael age: 22 average grade: 59.00
#input 3 Moore,Michael,22,96,88,82 output 3 Moore, Michael age: 22 average grade: 88.67
