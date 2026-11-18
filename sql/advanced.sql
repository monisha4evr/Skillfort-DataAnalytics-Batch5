-- subquery
-- query written inside another query 
-- outer query -> written outside 
-- inner query -> written Inside 

types 
1. correlation subquery (inner query run based on iuter query)
2. non -correlation subquery (inner query run independently)
	1. scalar subquery / single row subquery 
	2. inline/derived subquery / multi row subquery 
	3. multi-column subquery 
	
select * from demo.employees;
select * from "emp_attendance";


CREATE TABLE demo.employees_corr (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    salary INT,
    dept_id INT
);


INSERT INTO demo.employees_corr VALUES
(1,'Arun',25000,10),
(2,'Bala',30000,10),
(3,'Charan',35000,10),
(4,'Divya',40000,10),
(5,'Eswar',45000,10),
(6,'Farah',28000,10),
(7,'Gokul',32000,10),
(8,'Hari',50000,10),
(9,'Indhu',38000,10),
(10,'Jaya',42000,10),
(11,'Karthik',30000,20),
(12,'Lakshmi',45000,20),
(13,'Manoj',55000,20),
(14,'Nithya',60000,20),
(15,'Omkar',35000,20),
(16,'Priya',48000,20),
(17,'Rahul',65000,20),
(18,'Sneha',52000,20),
(19,'Tarun',70000,20),
(20,'Uma',40000,20),
(21,'Vijay',32000,30),
(22,'Waseem',38000,30),
(23,'Xavier',42000,30),
(24,'Yamini',50000,30),
(25,'Zara',45000,30),
(26,'Ajay',55000,30),
(27,'Bhavana',60000,30),
(28,'Chandru',35000,30),
(29,'Deepa',48000,30),
(30,'Elan',52000,30),
(31,'Fathima',28000,40),
(32,'Ganesh',33000,40),
(33,'Hema',37000,40),
(34,'Irfan',42000,40),
(35,'Janani',45000,40),
(36,'Kavin',50000,40),
(37,'Lavanya',55000,40),
(38,'Mohan',60000,40),
(39,'Naveen',35000,40),
(40,'Oviya',48000,40),
(41,'Pranav',30000,50),
(42,'Rani',36000,50),
(43,'Sanjay',40000,50),
(44,'Thara',45000,50),
(45,'Uday',50000,50),
(46,'Varun',55000,50),
(47,'Wasim',60000,50),
(48,'Yogesh',65000,50),
(49,'Zubin',38000,50),
(50,'Anu',42000,50);

-- correlation:
select * from demo.employees_corr;

select avg(salary) from demo.employees_corr e2 where dept_id=10;

select * from demo.employees_corr as e1 
where e1.salary < ( select avg(salary) from demo.employees_corr e2)

select * from demo.employees_corr as e1 
where e1.salary < ( select avg(salary) from demo.employees_corr e2 where e1.dept_id = e2.dept_id)


-- max 
select * from  demo.employees_corr e1 where salary=
(select max(salary) from demo.employees_corr e2  where e1.dept_id = e2.dept_id);


select * from  demo.employees_corr e1 where salary=
(select max(salary) from demo.employees_corr e2);


-- select * from  demo.employees_corr e1 where exists
-- (select  1 from demo.employees_corr e2 
-- where e2.dept_id=e1.dept_id and e2.salary > 60000);


select * from (
select dept_id,max(salary)as salary from demo.employees_corr group by dept_id)  as depart_salry;


-- multiple column subquery 
select emp_name,dept_id,salary from demo.employees_corr where (dept_id,salary) in (
select dept_id,salary from demo.employees_corr ) ;



-- using in having
select dept_id,avg(salary) 
from demo.employees_corr 
group by dept_id
having avg(salary) > ( select avg(salary) from demo.employees_corr );

-- subquery in where 

select emp_name,salary  
from demo.employees_corr 
where 
salary = (select max(salary) from demo.employees_corr)

-- subquery in select 
select emp_name,salary,(select max(salary) from demo.employees_corr) 
from demo.employees_corr;

-- 
select emp_name,dept_id,salary from demo.employees_corr
where (dept_id,salary) in (
	(10,25000)
)




CTE -- Common table Expression 
-- temporary named result set 
-- we can use that inside a SQL
-- write complex query in simple and readable way 

Syntax: 

with cte_name as (
	select * from table_name
)
select * from cte_name;

select * from demo.employees_corr;

with avg_salary as (
select avg(salary) as averageSal from demo.employees_corr)
select * from demo.employees_corr where salary > (select averageSal from avg_salary);

with max_sal as (
	select max(salary) as highest_salary from demo.employees_corr
)
select * from demo.employees_corr where salary =(select highest_salary from max_sal );

with dept_avg as (
	select dept_id,avg(salary) as avg_sal from demo.employees_corr group by dept_id
)
select * from dept_avg;


 with dept_avg as (
	select dept_id,avg(salary) as avg_sal from demo.employees_corr group by dept_id
 )
 select emp.* 
 from demo.employees_corr as emp
 join dept_avg d 
 on emp.dept_id = d.dept_id 
 where emp.salary>d.avg_sal;
 


View
--	virtual table - by sql query (saved sql query)
-- it doesn't store actual data  
-- it stores sql query and display result from original table.

syntax: 
-- create view view_name as select query

create view demo.high_sal_emp as 
select * from demo.employees_corr where dept_id=10 and salary >=50000;

select * from demo.high_sa

l_emp;


ACID PROPERTY
-- 
A - Atomicy (all or nothing)
C - Consistency (must follow the rules - contraints)
I - Isolation (independent transaction)
D - Durablity (permanent)


Normalization
--
-- organizing data in database 
-- reduce duplication

department
depart_id name
101 python
102 java
103 data Analytics

without normalization
student -> id name dept_id, department

with normalization
student -> id name dept_id 
department -> dept_id,department

1. first normal form (1NF)  (one cell = one value)
atomic - single
2. second normal form (2NF)
must satisfy 1NF 
no partial dependency
3. 3NF 
must satisfy 2NF 
no transitive dependency 



