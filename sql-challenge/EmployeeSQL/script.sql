/*drop table if exists departments;
drop table if exists dept_emp;
drop table if exists dept_manager;
drop table if exists employees;
drop table if exists salaries;
drop table if exists titles;
*/

create table departments (
	dept_no varchar(30) not null,
	dept_name varchar(30) not null
);

create table dept_emp (
	emp_no int not null,
	dept_no varchar(30) not null
);

create table dept_manager (
	dept_no varchar (30) not null,
	emp_no int not null
);

create table employees (
	emp_no int not null,
	emp_title_id varchar(30) not null,
	birth_date date not null,
	first_name varchar(30) not null,
	last_name varchar(30) not null,
	sex varchar(30) not null,
	hire_date date not null
);

create table salaries (
	emp_no int not null,
	salary int not null
);

create table titles (
	title_id varchar(30) not null,
	title varchar(30) not null
);