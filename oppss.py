
class student:
    company_name = 'abcd'

    @staticmethod
    def detail(name):
        print(f'my name is {name}')

    @classmethod
    def display_company(company):
        print(f'my company is {company.company_name}')

student.detail('Antony')
student.display_company()
