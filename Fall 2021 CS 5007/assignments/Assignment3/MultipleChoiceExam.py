from ITExam import ITExam


class MultipleChoiceExam(ITExam):
    POINTS_PER_QUESTION = 2

    def __init__(self):
        # super().__init__() #  not required since super class constructor does not have input args
        self.__num_mcq = 0
        self.__correct_num_mcq = 0

    def setTotalNumOfMCQuestion(self, num_of_mcq):
        #  check and assign the valid number
        #  return true or false
        if 0 < num_of_mcq <= 50:
            self.__num_mcq = num_of_mcq
            return True
        return False

    def getTotalNumOfQuestion(self):
        #  return number
        return self.__num_mcq

    def setCorrectNumOfMCQuestion(self, correct_mcq):
        #  check and assign valid number
        #  return T or F
        if 0 <= correct_mcq <= self.__num_mcq:
            self.__correct_num_mcq = correct_mcq
            return True
        return False

    def getCorrectNumOfMCQuestion(self):
        # return num of correct Q
        return self.__correct_num_mcq

    def getExamGrade(self):
        #  return grade based on score
        super().setExamScore(self.POINTS_PER_QUESTION * self.__correct_num_mcq)
        return super().getExamGrade()

    def toString(self):
        #  return exam title and score
        final_grade = self.getExamGrade()
        s = ""
        s += super().toString()
        s += "\nTotal Number of MC Questions: " + str(self.getTotalNumOfQuestion())
        s += "\nTotal Number of Correct MC Questions: " + str(self.getCorrectNumOfMCQuestion())
        s += "\nFinal Grade: " + final_grade

        return s


mce_object = MultipleChoiceExam()
