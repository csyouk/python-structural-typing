from zope.interface import Interface, Attribute, implementer

class IEmployee(Interface):
    name = Attribute("Name of employee")

    def do(work):
        """Do some work"""

@implementer(IEmployee)
class Employee:

    name = 'Anonymos'

    def do(self, work):
        return work.start()


class Worker:
    def start(self):
        print("Work start!!")

def main():
    work_instance = Worker()

    employee = Employee()
    employee.do(work_instance)

if __name__ == "__main__":
    main()