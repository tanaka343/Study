name='yamada'

class SchoolReport:
    school_name='サプー中学'
    def __init__(self,student_name,math_score,jp_score,en_score):
        self.student_name =student_name
        self.math_score =math_score
        self.jp_score = jp_score
        self.en_score = en_score

    def average(self):
        self.score= self.math_score + self.jp_score + self.en_score
        avg = self.score/3
        return avg


sr=SchoolReport('tanaka',100,100,100)
sr1=SchoolReport('naka',100,0,100)
print(f"{sr.student_name}:{sr.average()}")
print(f"{sr1.student_name}:{sr1.average()}")

print(SchoolReport.school_name)
print(sr.school_name)
sr.average()
print(sr.score)