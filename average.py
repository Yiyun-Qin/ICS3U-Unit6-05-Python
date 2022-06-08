#!/usr/bin/env python3

# Created by Yiyun Qin
# Created in June 2022
# This is the math program, calculating the average of marks


def average(marks):
    # This function calculates the average of marks
    total = 0
    for a_mark in marks:
        total = total + a_mark
    average_mark = total / len(marks)
    return average_mark


def main():
    # This function does try and catch
    marks = []
    a_mark_string = None

    # input
    print("Please enter 1 mark at a time. Enter -1 to end.")

    # process & output
    print("")
    while a_mark_string != "-1":
        a_mark_string = input("What is your mark? (as %): ")
        try:
            a_mark = int(a_mark_string)
            if a_mark >= 0 and a_mark <= 100:
                marks.append(a_mark)
            elif a_mark == -1:
                a_mark_string = str(a_mark)
                marks.append(a_mark)
                continue
            else:
                print("Please enter a score between 0 and 100!")
            a_mark_string = str(a_mark)
        except:
            print("Invalid number!")
    # remove the last thing in the list
    marks.pop()
    # call functions
    average_mark = average(marks)
    print("\nThe average is {:,.2f}%".format(average_mark))
    print("\nDone.")


if __name__ == "__main__":
    main()
