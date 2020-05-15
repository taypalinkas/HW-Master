--List all employees whose first name is "Hercules" and last names begin with "B."

select first_name, last_name
from employees
where first_name='Hercules' and last_name like 'B%';
