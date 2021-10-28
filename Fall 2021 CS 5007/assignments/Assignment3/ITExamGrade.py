from ITExam import ITExam
from MultipleChoiceExam import MultipleChoiceExam
from TechnicalWritingExam import TechnicalWritingExam
from AnalyticalProgrammingExam import AnalyticalProgrammingExam


def fillITExam(oneExamObject):
    if isinstance(oneExamObject, MultipleChoiceExam):
        #  Prompt user

    elif isinstance(oneExamObject, TechnicalWritingExam):
        #  Prompt user

    elif isinstance(oneExamObject, AnalyticalProgrammingExam):
        #  Prompt user

    return oneExamObject


def displayResults(allExamList):
    s =""
    return s


def main():
    # Storing exam menu as string object
    exam_menu = ""
    exam_menu += "\nIT Exam Type Menu:"
    exam_menu += "\n1) Multiple Choice"
    exam_menu += "\n2) Technical Writing"
    exam_menu += "\n3) Analytical Programming"
    exam_object_list = []

    choice_flag = True  # input validation flag for exam choice
    exam_flag = True  # flag is true if more exams exist
    choice_error = "Sorry! No such choice. Please enter it again"
    # title_error = "Sorry! The exam title is not valid. Please enter it again"
    # num_error = "\nSorry! The number is not valid. Please enter it again."
    # score_error = "\nSorry! The score is not valid. Please enter it again"

    while exam_flag:
        #  Display exam menu
        print(exam_menu)

        #  Prompt user for exam choice
        choice = int(input("Enter your choice: "))
        if 0 >= choice >= 4:
            print(choice_error)
            choice_flag = False

        if choice == 1:
            exam_object = MultipleChoiceExam()
        elif choice ==2:
            exam_object = TechnicalWritingExam()
        elif choice ==3:
            exam_object = AnalyticalProgrammingExam()

        # Fill exam object
        oneExamObject = fillITExam(exam_object)

        # Append exam object to list
        exam_object_list.append(oneExamObject)

        # Check if more IT Exams
        more_exam = input("More IT Exams (Yes/No)? ")
        if more_exam == "Yes":
            exam_flag = True
        else:
            exam_flag = False

    # Format output
    s = displayResults(exam_object_list)

    # Display output
    print(s)

        # if choice_flag:
        #     exam_title = input("\nEnter the Exam Title: ")
        #     while not ITExam.setExamTitle(exam_title):
        #         print(title_error)
        #         exam_title = input("\nEnter the Exam Title: ")
        #
        #     if choice == 1:
        #         num_flag = False
        #         mcq_flag = False
        #
        #         while not num_flag:
        #             try:
        #                 mcq_num = int(input("Total Number of Multiple Choice's Questions: "))
        #                 num_flag = True
        #             except ValueError:
        #                 print(num_error)
        #
        #         while not mcq_flag:
        #             if MultipleChoiceExam.setTotalNumOfMCQuestion(mcq_num):
        #                 mcq_flag = True
        #
        #
        #
        #
        #     elif choice == 2:
        #         num_flag = False
        #         score_flag = False
        #         while not num_flag:
        #             try:
        #                 grammer_score = int(input("Score of Grammer Potion: "))
        #                 num_flag = True
        #             except ValueError:
        #                 print(num_error)
        #
        #         score_flag = TechnicalWritingExam.setGrammerScore(grammer_score)
        #         while not score_flag:
        #             print(score_error)
        #             score_flag = TechnicalWritingExam.setGrammerScore(grammer_score)




if __name__ == "__main__":
    main()
