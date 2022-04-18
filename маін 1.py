class student:
    def __init__(self, name, Age, money, birthday, work):
        self.name = Іван
        self.Age  = 18 
        self.money = 0
        self.hunger = True
        
    def about (self):
        print('Студента звати:' + self.name)
        print("Cтуденту " + str(self.Age))
        print("у студента" + str(self.money))

    def work(self):
        print("Студент пішов на роботу")
        self.money = self.money + 10

    def feed(self):
        if self.hunger:
            print("Студент наївся")
            self.hunger = False
        else:
            print('Студент не голодний')

    def sleep(self):
        print("Студент спить")
        self.hunger = True

    def get_up(self):
        print('Студент прокинувся')

    def study(self):
        print('Студент вчится')

student = student()

student.about()
student.feed()
student.sleep()
student.get_up()
student.work()