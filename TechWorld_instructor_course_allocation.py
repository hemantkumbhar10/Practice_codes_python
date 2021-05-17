class Instructor:
    def __init__(self, instructor_name, technology_skill, experience, avg_feedback):
        self.__instructor_name = instructor_name
        self.__technology_skill = technology_skill
        self.__experience = experience
        self.__avg_feedback = avg_feedback

    def set_instructor_name(self):
        self.__instructor_name = instructor_name

    def set_technology_skill(self):
        self.__technology_skill = technology_skill

    def set_experience(self):
        self.__avg_feedback = avg_feedback

    def get_instructor_name(self):
        return self.__instructor_name

    def get_technology_skill(self):
        return self.__technology_skill

    def get_experience(self):
        return self.__experience

    def get_avg_feedback(self):
        return self.__avg_feedback

    def check_eligibility(self):
        if self.__experience > 3:
            eligible = True
        else:
            eligible = False
        return eligible

    def allocate_course(self, technology):
        for i in self.__technology_skill:
            if i == technology:
                allocate = True
            else:
                continue
            return allocate
ls = ['python', 'java', 'c']
c1 = Instructor('jay',ls, 4, 4.7)
print(c1.allocate_course('java'))