from ITExam import ITExam


class TechnicalWritingExam(ITExam):
    MAX_SCORE = 100
    GRAMMER_PERCENT = 0.3
    SENTENCE_PERCENT = 0.3
    CONTENT_PERCENT = 0.4

    def __init__(self):
        self.__grammer_score = 0
        self.__sentence_structure_score = 0
        self.__content_score = 0

    def setGrammerScore(self, grammer_score):
        #  validate and assign score
        # return T or F

        if 0 <= grammer_score <= self.MAX_SCORE:
            self.__grammer_score = grammer_score
            return True
        return False

    def getGrammerScore(self):
        #  ret score
        return self.__grammer_score

    def setSentenceStructureScore(self, sentence_structure_score):
        # validate and assign score
        # ret T or F
        if 0 <= sentence_structure_score <= self.MAX_SCORE:
            self.__sentence_structure_score = sentence_structure_score
            return True
        return False

    def getSentenceStructureScore(self):
        #  ret score
        return self.__sentence_structure_score

    def setContentScore(self, content_score):
        #  validate and assign score
        #  ret T or F
        if 0 <= content_score <= self.MAX_SCORE:
            self.__content_score = content_score
            return True
        return False

    def getContentScore(self):
        #  ret score
        return self.__content_score

    def getExamGrade(self):
        #  ret grade based on score
        super().setExamScore((self.GRAMMER_PERCENT * self.__grammer_score) +
                             (self.SENTENCE_PERCENT * self.__sentence_structure_score) +
                             (self.CONTENT_PERCENT * self.__content_score))
        return super().getExamGrade()

    def toString(self):
        #  return exam title and score
        final_grade = self.getExamGrade()
        s = ""
        s += super().toString()
        s += "\nScore of Grammer Portion: " + str(round(float(self.getGrammerScore()), 1))
        s += "\nScore of Sentence Structure Portion: " + str(round(float(self.getSentenceStructureScore()), 1))
        s += "\nScore of Content Portion: " + str(round(float(self.getContentScore()), 1))
        s += "\nFinal Grade: " + final_grade

        return s


twe_obj = TechnicalWritingExam()
