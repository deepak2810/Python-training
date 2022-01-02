
# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.


emp_year_of_service = int(input('please enter your year of service'))

if emp_year_of_service>=5: 
 emp_salary=int(input('enter your salary : '))
 salary_increment = ((emp_salary*5)/100)
 new_salary = emp_salary+salary_increment
 print('congratulations ! your new salary is ' , new_salary)
 print('enjoy')

else:
    print(' salary can not be incremented now as you have not match our salary incremented crieteria.')
    print('see you soon.')

