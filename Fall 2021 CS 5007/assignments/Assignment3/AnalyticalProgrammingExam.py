from ITExam import ITExam


class AnalyticalProgrammingExam(ITExam):
    MAX_SCORE = 100
    SHORT_ANSWER_PERCENT = 0.3
    PROGRAMMING_PERCENT = 0.7

    def __init__(self):
        # super().__init__()
        self.__short_answer_score = 0
        self.__programming_score = 0

    def setShortAnswerScore(self, short_answer_score):
        #  validate and assign score
        #  ret T or F
        if 0 <= short_answer_score <= self.MAX_SCORE:
            self.__short_answer_score = short_answer_score
            return True
        return False

    def getShortAnswerScore(self):
        #  ret score
        return self.__short_answer_score

    def setProgrammingScore(self, programming_score):
        #  validate and assign score
        #  ret T or F
        if 0 <= programming_score <= self.MAX_SCORE:
            self.__programming_score = programming_score
            return True
        return False

    def getProgrammingScore(self):
        #  ret score
        return self.__programming_score

    def getExamGrade(self):
        #  ret grade based on score
        super().setExamScore((self.SHORT_ANSWER_PERCENT * self.__short_answer_score) +
                             (self.PROGRAMMING_PERCENT * self.__programming_score))
        return super().getExamGrade()

    def toString(self):
        #  return exam title and score
        final_grade = self.getExamGrade()
        s = ""
        s += super().toString()
        s += "\nScore of Short Answer Section: " + str(round(float(self.getShortAnswerScore()), 1))
        s += "\nScore of Programming Section: " + str(round(float(self.getProgrammingScore()), 1))
        s += "\nFinal Grade: " + final_grade

        return s


ape_object = AnalyticalProgrammingExam()
