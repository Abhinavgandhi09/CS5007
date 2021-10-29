from MultipleChoiceExam import MultipleChoiceExam
from TechnicalWritingExam import TechnicalWritingExam
from AnalyticalProgrammingExam import AnalyticalProgrammingExam


def fillITExam(oneExamObject):
    #  Prompt user for title
    title_flag = False #  True when title is valid

    while not title_flag:
        title = input("\nEnter the exam title: ")
        if oneExamObject.setExamTitle(title):
            title_flag = True
        else:
            print("Sorry! The exam title is not valid. Please enter it again")

    if isinstance(oneExamObject, MultipleChoiceExam):
        # Prompt user for total mcquestions
        num_flag = False #  True when total number of mcq is valid

        while not num_flag:
            num_mcq = int(input("Total Number of Multiple Choice: "))
            if oneExamObject.setTotalNumOfMCQuestion(num_mcq):
                num_flag = True
            else:
                print("\nSorry! The number is not valid. Please enter it again.")

        # Prompt user for num of correct mcquestions
        num_correct_flag = False #  True when number of correct mcq is valid

        while not num_correct_flag:
            num_correct_mcq = int(input("Total Number of Correct Multiple Choice's Questions: "))
            if oneExamObject.setCorrectNumOfMCQuestion(num_correct_mcq):
                num_correct_flag = True
            else:
                print("\nSorry! The number is not valid. Please enter it again")

    elif isinstance(oneExamObject, TechnicalWritingExam):
        #  Prompt user for grammer score
        grammer_flag = False #  True when grammer score is valid

        while not grammer_flag:
            gram_score = int(input("Score of Grammer Portion: "))
            if oneExamObject.setGrammerScore(gram_score):
                grammer_flag = True
            else:
                print("\nSorry! The score is not valid. Please enter it again.")

        #  Prompt user for sentence str score
        sent_str_flag = False  # True when sentence structure score is valid

        while not sent_str_flag:
            sent_str_score = int(input("Score of Sentence Structure Portion: "))
            if oneExamObject.setSentenceStructureScore(sent_str_score):
                sent_str_flag = True
            else:
                print("\nSorry! The score is not valid. Please enter it again.")

        #  Prompt user for content score
        content_flag = False #  True when content score is valid

        while not content_flag:
            content_score = int(input("Score of Content Portion: "))
            if oneExamObject.setContentScore(content_score):
                content_flag = True
            else:
                print("\nSorry! The score is not valid. Please enter it again.")

    elif isinstance(oneExamObject, AnalyticalProgrammingExam):
        #  Prompt user for short ans score
        short_ans_flag = False #  True when short answer score is valid

        while not short_ans_flag:
            short_ans_score = int(input("Score of Short Answer Section: "))
            if oneExamObject.setShortAnswerScore(short_ans_score):
                short_ans_flag = True
            else:
                print("\nSorry! The score is not valid. Please enter it again.")

        #  Prompt user for programming score
        prog_flag = False #  True when programming score is valid

        while not prog_flag:
            prog_score = int(input("Score of Programming Section: "))
            if oneExamObject.setProgrammingScore(prog_score):
                prog_flag = True
            else:
                print("\nSorry! The score is not valid. Please enter it again.")

    return oneExamObject


def displayResults(allExamList):
    s =""
    total_score = 0
    exam_count = 0

    for exam_obj in allExamList:
        s += exam_obj.toString()
        total_score += exam_obj.getExamScore()
        exam_count += 1

    s += "\n\nTotal Score of All Exams: " + str(round(float(total_score), 1))
    s += "\nAverage Score of All Exams: " + str(round(total_score/exam_count, 1))

    return s


def main():
    # Storing exam menu as string object
    exam_menu = ""
    exam_menu += "\nIT Exam Type Menu:"
    exam_menu += "\n1) Multiple Choice"
    exam_menu += "\n2) Technical Writing"
    exam_menu += "\n3) Analytical Programming"
    exam_object_list = []

    exam_flag = True  # flag is true if more exams exist

    while exam_flag:
        #  Display exam menu
        print(exam_menu)

        #  Prompt user for exam choice
        choice_flag = False
        choice = None

        while not choice_flag:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= 3:
                choice_flag = True
            else:
                print("\nSorry! No such choice. Please enter it again.")

        #  Creating relevant exam object based on choice
        exam_object = None

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
        more_exam = input("\nMore IT Exams (Yes/No)? ")
        if more_exam == "Yes":
            exam_flag = True
        else:
            exam_flag = False

    # Format output
    s = displayResults(exam_object_list)

    # Display output
    print(s)


if __name__ == "__main__":
    main()
