class Medical:
    
    def __init__(self, name, age, sex, bmi, n_children, smoker):
        self.name = name
        self.age = age
        self.sex = sex  # 0 for male, 1 for female
        self.bmi = bmi
        self.n_children = n_children
        self.smoker = smoker  # 0 non smoker, 1 smoker

    def estimated_insurance_cost(self):
        cost = (250 * self.age) - (128 * self.sex) + (370 * self.bmi) +(425 * self.n_children) + (24000 * self.smoker) - 12500
        print(f'{self.name} estimated insurance cost is {cost} dollars')

    def update_age(self, new_age):
        self.age = new_age
        print(f'{self.name} id now {self.age} years old')

    def update_children(self, new_n_children):
        self.n_children = new_n_children
        if self.n_children == 1:
            print(f'{self.name} has {self.n_children} children')
        else:
            print(f'{self.name} has {self.n_children} childrens')

    def patient_information(self):
        info = {}
        info['name'] = self.name
        info['age'] = self.age
        info['sex'] = self.sex
        info['bmi'] = self.bmi
        info['n_children'] = self.n_children
        info['smoker'] = self.smoker
        return info
            


patient1 = Medical('Mateo', 26, 0, 22, 0, 1)
#print(patient1.name)
patient1.estimated_insurance_cost()
patient1.update_age(27)
patient1.update_children(2)
print(patient1.patient_information())