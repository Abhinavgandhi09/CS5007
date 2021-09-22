
def compute_student_statistics(exam_scores, exam_count, student_num, result):
    # Computing avg score
    score_sum = 0
    for score in exam_scores:
        score_sum += score
    try:
        avg_score = score_sum/exam_count
    except ZeroDivisionError:
        avg_score = 0

    # Computing highest score
    try:
        max_score = max(exam_scores)
    except ValueError:
        max_score = 0

    # Computing lowest score
    try:
        min_score = min(exam_scores)
    except ValueError:
        min_score = 0

    result = result + "Student " + str(student_num) + " took " + str(exam_count) + " exams" + "\n"
    result = result + "Average score: " + str(round(avg_score, 2)) + "\n"
    result = result + "Highest score: " + str(max_score) + "\n"
    result = result + "Lowest score: " + str(min_score) + "\n" + "\n"
    return result


def main():
    # ------------------------- Declaring required variables ----------------------
    student = True  # variable to check if there are any more students
    student_count = 0  # variable to count number of students
    score = 0  # variable to store input score
    flag = True  # input validation flag
    str_result = ""  # stores results

    # -------- Prompt user for student details, compute student's statistics --------

    while student:
        # Declare score_lst & score_count variables for each student
        score_lst = []
        score_count = 0

        student_count += 1  # Increase student count

        # Receive student's score from user input
        try:
            score = float(input("Please enter student " + str(student_count) + "\'s score (-1: Exit): "))
        except ValueError:
            print("The score entered is not a number. Please enter it again.")
            print()
            flag = False

        while score != -1:

            if flag:  # Ensuring score is valid, if not prompt user again

                # Append score to list
                score_lst.append(score)
                score_count += 1  # Accumulator to count number of exams

            # Receive student's score from user input
            try:
                score = float(input("Please enter student  " + str(student_count) + "\'s score (-1: Exit): "))
                flag = True
            except ValueError:
                print("The score entered is not a number. Please enter it again.")
                print()
                flag = False

        # Compute student's statistics and store as string
        str_result = compute_student_statistics(score_lst, score_count, student_count, str_result)

        # Check whether any more students exist
        print()
        s = input("Any more student?(Yes or No): ")
        print()
        if s.upper() == "YES":
            student = True
        else:
            student = False

    # Print results
    print(str_result)


if __name__ == "__main__":
    main()
