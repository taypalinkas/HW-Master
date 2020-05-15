/*list the department of each employee with the following information:
employee number, last name, first name, and department name.
*/

select dept_emp.emp_no, employees.first_name, employees.last_name, departments.dept_name
from dept_emp
join departments on dept_emp.dept_no=departments.dept_no
join employees on dept_emp.emp_no=employees.emp_no;