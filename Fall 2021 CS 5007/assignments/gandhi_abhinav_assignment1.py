

def main():

    # ------------------------- Declaring required variables ----------------------
    student = True  # variable to check if there are any more students
    count = 1  # variable to count number of students
    score_lst = []  # list to store student scores
    score = 0  # variable to store input score
    score_count = 0  # variable to count number of scores per student
    n_exam = []  # list to store number of exams per student
    s = ""  # stores string entered by user
    offset = 0  # variable to iterate through scores list
    max_score = 0  # variable to store Highest score
    min_score = 10000  # variable to store Lowest score
    score_sum = 0  # variable to store sum of a students scores

    # ------------------------- Prompt user for details and store ----------------------
    while student:
        while score != -1:

            # Receive student's score and append to list only if it is not -1
            try:
                score = float(input("Please enter student "+str(count)+"\'s score (-1: Exit): "))
            except ValueError:
                print("The score entered is not a number. Please enter it again.")
                score = float(input("Please enter student "+str(count)+"\'s score (-1: Exit): "))

            if score != -1:
                score_lst.append(score)
                score_count += 1  # count number of exams

        # Store the number of exams to the list n_exam
        n_exam.append(score_count)

        # Reset score & score_count for next student
        score_count = 0
        score = 0

        # Check whether any more students exist
        print()
        s = input("Any more student?(Yes or No): ")
        print()
        if s == "Yes":
            student = True
        else:
            student = False

        # Increase student count if student exists
        if student:
            count += 1

    # ------------------------------ Compute and print results -----------------------
    for i in range(1, count+1, 1):  # Here i is student number
        print("Student ", i, "took ", (n_exam[i - 1]), " exams")

        for j in range(n_exam[i - 1]):
            score_sum = score_sum + score_lst[offset + j]  # sum of student i's scores

            if score_lst[offset + j] > max_score:  # Highest score of student i
                max_score = score_lst[offset + j]

            if score_lst[offset + j] < min_score:  # Lowest score of student i
                min_score = score_lst[offset + j]

        offset += n_exam[i - 1]  # index offset for next student's scores
        # This accounts for the offsets due to the '-1' in the list
        try:
            avg = 1.0*score_sum/(n_exam[i - 1])  # avg score for student i
        except ZeroDivisionError:
            avg = 0
            min_score = 0

        print("Average score: ", round(avg, 2))
        print("Highest score: ", max_score)
        print("Lowest score: ", min_score)
        print()

        # Reset max and min score and score sum
        max_score = 0
        min_score = 10000
        score_sum = 0


if __name__ == "__main__":
    main()