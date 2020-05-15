/*In descending order, list the frequency count of employee last names,
i.e., how many employees share each last name.
*/

select last_name, count(last_name)
from employees
group by last_name
order by count(last_name) desc;