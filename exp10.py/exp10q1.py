class Employee:
    def __init__(self, empid, name, basic_pay):
    
        self.empid = empid
        self.name = name
        self.basic_pay = basic_pay
        self.ta = 0
        self.da = 0
        self.gross_pay = 0

   
    def calc(self):
        self.ta = 0.10 * self.basic_pay      
        self.da = 0.40 * self.basic_pay     
        self.gross_pay = self.basic_pay + self.ta + self.da

    def disp(self):
        print("\nEmployee ID:", self.empid)
        print("Employee Name:", self.name)
        print("Basic Pay:", self.basic_pay)
        print("TA (10%):", self.ta)
        print("DA (40%):", self.da)
        print("Gross Pay:", self.gross_pay)



empid = int(input("Enter Employee ID: "))
name = input("Enter Employee Name: ")
basic_pay = float(input("Enter Basic Pay: "))

emp = Employee(empid, name, basic_pay)

emp.calc()   
emp.disp()   