class ITExam:

    MAX_SCORE = 100

    def __init__(self):
        self.__exam_title = None
        self.__exam_score = 0

    def setExamTitle(self, title):
        #  Checking if exam title is not null and assigning to instance variable
        #  return T or F
        if title:
            self.__exam_title = title
            return True
        else:
            return False

    def getExamTitle(self):
        #  return exam title
        return self.__exam_title

    def setExamScore(self, score):
        #  check and assign valid score to instance variable
        #  return T or F
        if 0 <= score <= self.MAX_SCORE:
            self.__exam_score = score
            return True
        else:
            return False

    def getExamScore(self):
        #  return exam score
        return self.__exam_score

    def getExamGrade(self):
        #  return grade based on score

        # Set a default value for exam_grade
        exam_grade = 'F'

        if self.__exam_score >= 90:
            exam_grade = 'A'
        elif self.__exam_score >= 80:
            exam_grade = 'B'
        elif self.__exam_score >= 70:
            exam_grade = 'C'
        elif self.__exam_score >= 60:
            exam_grade = 'D'

        return exam_grade

    def toString(self):
        #  return exam title and score
        s = ""
        s += "\n\nExam Title: " + self.getExamTitle()
        s += "\nExam Score: " + str(round(float(self.getExamScore()), 1))

        return s


ite_obj = ITExam()
