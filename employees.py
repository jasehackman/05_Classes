# Create a class that contains information about employees of a company and define methods to get/set employee name, job title, and start date.
import datetime
now = datetime.datetime.now()


class Employee:
  def __init__(self, hireDate = now):
    self.__startDate = hireDate

  @property
  def name(self):
    try:
      return self.__name
    except:
      print("add a name")

  @name.setter
  def name(self,name):
    self.__name = name

  @property
  def job_title(self):
    try:
      return self.__job_title
    except:
      print("no job title")

  @job_title.setter
  def job_title(self, title):
    self.__job_title = title

  @property
  def startDate(self):
    try:
      return self.__startDate
    except:
      print("no start date")

  @startDate.setter
  def startDate(self, date):
    self.__startDate = date

  def __str__(self):
    return f"this employee's name is {self.__name}"


bob = Employee()

bob.name = "bob"

bob.job_title = "janitor"


print(bob)
# Copy this Company class into your module.

class Company(object):
    """This represents a company in which people work"""

    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded
        self.employees = set()

    def get_company_name(self):
        """Returns the name of the company"""

        return self.company_name

    def employeePrint (self):
      [print(employee.name) for employee in self.employees]

    def __str__(self):
      return f"Company's name is {self.company_name} and its employees are {print(customer) for customer in self.employees}"

#     # Add the remaining methods to fill the requirements above
# Consider the concept of aggregation, and modify the Company class so that you assign employees to a company.

# Create a company, and three employees, and then assign the employees to the company.

NSS = Company("NSS", "2013")
jim = Employee()
mike = Employee()

jim.name = "jim"
mike.name = "Greg"

NSS.employees.add(jim)
NSS.employees.add(mike)

NSS.employeePrint()

