/*List all employees in the Sales and Development departments, 
including their employee number, last name, first name, and department name.
*/

select dept_emp.emp_no, employees.last_name, employees.first_name, departments.dept_name
from dept_emp
join employees on dept_emp.emp_no=employees.emp_no
join departments on dept_emp.dept_no=departments.dept_no
where departments.dept_name = 'Sales' or departments.dept_name = 'Development';