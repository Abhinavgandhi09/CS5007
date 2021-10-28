from ITExam import ITExam


class MultipleChoiceExam(ITExam):
    POINTS_PER_QUESTION = 2

    def __init__(self):
        # super().__init__()
        self.__num_mcq = 0
        self.__correct_num_mcq = 0

    def setTotalNumOfMCQuestion(self, num_of_mcq):
        #  check and assign the valid number
        #  return true or false
        if num_of_mcq > 0:
            self.__num_mcq = num_of_mcq
            return True
        return False

    def getTotalNumOfQuestion(self):
        #  return number
        return self.__num_mcq

    def setCorrectNumOfMCQuestion(self, correct_mcq):
        #  check and assign valid number
        #  return T or F
        if correct_mcq >= 0:
            self.__correct_num_mcq = correct_mcq
            return True
        return False

    def getCorrectNumOfMCQuestion(self):
        # return num of correct Q
        return self.__correct_num_mcq

    def getExamGrade(self):
        #  return grade based on score
        self.setExamScore(self.POINTS_PER_QUESTION * self.__correct_num_mcq)
        return super().getExamGrade()

    def toString(self):
        #  return exam title and score
        # s = ""
        # s += "\nExam Title: " + self.getExamTitle()
        # s += "\nExam Score: " + self.getExamScore()
        return super().toString()


mce_object = MultipleChoiceExam()
