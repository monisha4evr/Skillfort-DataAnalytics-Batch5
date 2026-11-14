-- Object: Manage the Structure eg: table,view,schema
/*
SQL command 
1. DDL - Data Definition Language
2. DML - Data Manipulation Language
3. DQL - Data Query Language
4. DCL - Data Control Language
5. TCL - Transaction Control Language 

DDL - Data Definition Language (Manage Structure of Database)
-- CREATE ALTER DROP TRUNCATE
SYNTAX:
CREATE DATABASE DATABASE_NAME
*/

CREATE TABLE TABLENAME (
field_name data_type
)
-- sql 

create table demo.product(
id int primary key,
product_name varchar(50),
brand varchar(50)
);

create table demo.product(
id serial primary key,
product_name varchar(50),
brand varchar(50)
);

-- Note: Generated always as Identity  - can not add primary key column by manual
-- 2. Genereated default as Identity - we can give value to primary key column

create table demo.product(
id int generated always as identity  primary key,
product_name varchar(50),
brand varchar(50)
);

drop table demo.product;

insert into demo.product (product_name) values('banana');

select * from demo.product;

-- to set AutoIncrement 
-- serial 

create schema test;
Syntax: Create schema Schema_name;

drop schema test;




SET search_path TO public;

select current_database();

SELECT column_name, data_type, is_nullable
FROM information_schema.columns
WHERE table_schema = 'demo'
AND table_name = 'product';

-- ALTER

-- ALTER TABLE table_name action;
1. add a new column 
2. modify column data type 
3. rename a column 
4. drop Column 
5. rename to table 
6. add constraint 
7. drop constraint
-- product -> product_id product_name, price 

create table demo.product(
	product_id int generated always as identity primary key,
	product_name varchar(10),
	price bigint
);

select * from demo.product;
-- 1. add a new column 
alter table demo.product add column brand varchar(120);

-- char fixed length
-- varchar 

-- 2. modify column data type 
alter table demo.product alter column product_name type varchar(100);
alter table demo.product alter column product_name type text;


-- 3. rename a column 
alter table demo.product rename column product_name to prd_name;

4. drop a column

-- alter table demo.product add column cat varchar(10)

alter table demo.product drop column cat;


5. rename to table 

alter table demo.products rename to product;

6. add constraint 

ALTER TABLE demo.product 
    ADD CONSTRAINT prd_name_notnull CHECK (prd_name IS NOT NULL);
-- unique,check ,null,not null

7. Drop a Constraint

alter table demo.product drop constraint prd_name_notnull;


insert into demo.product (prd_name,brand,price) values ('car','Jaquar',2500000);

select * from demo.product;

-- truncate
-- DML :=> CRUD create/insert , Update ,delete
-- DQL :=> Data Query Language read 

-- insert (to add data into the table)
-- syntax: INSERT INTO TABLE_NAME (FIELD_NAME) VALUES () 

insert into demo.product (prd_name,price,brand) values 
('bike',2000000,'JAVA'),
('bike',2000000,'Splender'),
('toycar',3000000,'Monisha');

-- Syntax: update table_name set field_name=value where  condition
-- update demo.product set price=3000000 where product_id=1;
-- update demo.product set price=3500000 where product_id in(2,3);
-- update demo.product set price=2000000 where prd_name='car' and product_id<=3;


-- delete Row from table
-- Syntax: DELETE FROM TABLE_NAME where condition 

-- DELETE from demo.product where product_id=5;


select * from demo.product;

select * from demo.product where prd_name='car';
select prd_name,brand from demo.product where prd_name='car' and brand='Audi';


truncate table demo.product;



commit
Savepoint 1
Savepoint 2 
commit
Savepoint 3 
Savepoint 4 
Savepoint 5 
commit

rollback to 3

-- 
BEGIN;

-- Deduct money from Account A
UPDATE demo.product SET brand = 'Jaquar' WHERE id = 1;

-- Create a checkpoint
SAVEPOINT transfer_step;

-- Attempt to credit Account B
UPDATE demo.product  SET brand = 'Jaquar' WHERE id = 2;

-- If an error happens here, you can partial rollback:
-- ROLLBACK TO transfer_step;

-- Commit and save all changes permanently
COMMIT;


-- wildcard - ( % _ )


select * from demo.product where brand like 'm%';
select * from demo.product where brand like '%';
select * from demo.product where brand like '%r%';
select * from demo.product where brand like '_m_';
select prd_name,brand from demo.product where brand similar to '%[ru]%';
select prd_name,brand from demo.product where brand similar to '(mar|Ja)%';

select * from demo.product where brand ilike 'm%';


-- Data Maniplation
-- concatenation 

select concat('Hi',' ','welcome');

select prd_name,brand , concat(prd_name,'-',brand) from demo.product;

-- concat with seperator 

select concat_ws('-',prd_name,brand) from demo.product; -- null accept

-- format string 

select format('info:%s%s%I',prd_name,brand,price) from demo.product;

-- upper lower 
select upper(prd_name),lower(prd_name) from demo.product;

-- split the string Syntax: substring(column,start_pos,total_string) 
select brand, substring(brand,2,3) from demo.product;

select brand,length(brand) from demo.product;
-- trim, padding,replace,reverse,prefix,suffix,capitalize  

select 5*20;
select 100+5000;
select 500/3;

select round(abs(cos(90)));

select prd_name,price,round(price*0.1) as perct from demo.product;
select prd_name,price,round(price*110/100) as perct from demo.product;

-- datetime 

select current_date;
select current_time;
select current_date,current_time,current_timestamp;

-- intervals 
select current_date ,current_date - interval '30 days' as prev_date;

CREATE TABLE demo.student_details (
    student_id SERIAL PRIMARY KEY,
    student_name VARCHAR(50),
    course VARCHAR(50)
);

CREATE TABLE demo.attendance (
    attendance_id SERIAL PRIMARY KEY,
    student_id INT ,
    attendance_date DATE,
    status VARCHAR(20)
);

INSERT INTO demo.student_details (student_name, course)
VALUES
('Arun', 'Python'),
('Priya', 'Python'),
('Kumar', 'Python'),
('Divya', 'Python'),
('Rahul', 'Python');

INSERT INTO demo.attendance (student_id, attendance_date, status)
VALUES
(1, '2026-11-01', 'Present'),
(1, '2026-11-02', 'Present'),
(1, '2026-11-03', 'Absent'),
(1, '2026-11-04', 'Present'),
(1, '2026-11-05', 'Present'),
(2, '2026-11-01', 'Present'),
(2, '2026-11-02', 'Absent'),
(2, '2026-11-03', 'Present'),
(2, '2026-11-04', 'Present'),
(3, '2026-11-01', 'Absent'),
(3, '2026-11-02', 'Present'),
(3, '2026-11-03', 'Present'),
(4, '2026-11-01', 'Present'),
(4, '2026-11-02', 'Present'),
(4, '2026-11-03', 'Present'),
(5, '2026-11-01', 'Absent'),
(5, '2026-11-02', 'Absent');


CREATE TABLE demo.emp_attendance (
    attendance_id INT PRIMARY KEY,
    employee_id INT,
    employee_name VARCHAR(50),
    department VARCHAR(30),
    attendance_date DATE,
    check_in TIME,
    check_out TIME,
    status VARCHAR(20),
    working_hours DECIMAL(4,2)
);

INSERT INTO demo.emp_attendance  VALUES
(1, 101, 'Arun', 'IT', '2026-11-01', '09:00', '18:00', 'Present', 9),
(2, 102, 'Bala', 'HR', '2026-11-01', '09:30', '18:00', 'Present', 8.5),
(3, 103, 'Charan', 'Sales', '2026-11-01', NULL, NULL, 'Absent', 0),
(4, 104, 'David', 'IT', '2026-11-01', '09:15', '17:30', 'Present', 8.25),
(5, 105, 'Ezhil', 'Finance', '2026-11-01', '10:00', '18:00', 'Late', 8),
(6, 101, 'Arun', 'IT', '2026-11-02', '09:10', '18:00', 'Present', 8.83),
(7, 102, 'Bala', 'HR', '2026-11-02', NULL, NULL, 'Absent', 0),
(8, 103, 'Charan', 'Sales', '2026-11-02', '09:00', '18:00', 'Present', 9),
(9, 104, 'David', 'IT', '2026-11-02', '09:45', '18:00', 'Late', 8.25),
(10, 105, 'Ezhil', 'Finance', '2026-11-02', '09:00', '18:00', 'Present', 9),
(11, 101, 'Arun', 'IT', '2026-11-03', NULL, NULL, 'Absent', 0),
(12, 102, 'Bala', 'HR', '2026-11-03', '09:00', '18:00', 'Present', 9),
(13, 103, 'Charan', 'Sales', '2026-11-03', '09:20', '18:00', 'Late', 8.67),
(14, 104, 'David', 'IT', '2026-11-03', '09:00', '18:00', 'Present', 9),
(15, 105, 'Ezhil', 'Finance', '2026-11-03', NULL, NULL, 'Absent', 0);

select * from demo.emp_attendance where attendance_date ='2026-11-09';
select * from demo.emp_attendance where attendance_date >= current_date - interval '5 days';

select current_date - interval '5 months';

select current_date - interval '5 days';
select current_date - interval '1 years';

select extract(year from attendance_date) as year,
extract (month from attendance_date) as month from demo.emp_attendance;

select extract(day from current_timestamp) as day,
extract(month from current_timestamp) as month,
extract(year from current_timestamp),
extract ( day from current_date) as day;


select current_timestamp,current_timestamp :: date,current_timestamp :: time;
select cast(current_date as timestamp);


select '2026-11-12'::date - '2026-11-01'::date as date_diff;

select date_trunc('year',current_date);
select date_trunc('month',current_date);
select date_trunc('week',current_date);


-- Aggregation 

select * from public.payments;

select sum(paid) as total_amount  from public.payments;
select count(paid) as total_payment_count from public.payments;
select max(paid) as higest_amt from public.payments;
select min(paid) as higest_amt from public.payments;


select * from public.students;
select sum(age),count(city) from public.students;
select count(distinct(city)) from public.students;

select name,city from public.students order by city ; -- default : asc
select name,city from public.students order by city asc;
select name,city from public.students order by city desc;

select min(age) from public.students;
select * from public.students   offset 10; --pagination


-- group by

select city,count(city) as tot_count from public.students 
group by city order by tot_count desc;

select city from public.students 
group by city ;



select city,count(city) as tot_count from public.students  where age>=20
group by city  having count(city) < 7 order by tot_count desc;

select * from public.students;
select * from public.payments;

-- join 

-- cross join 
-- left join 
-- right join
-- inner join
-- self join 

--cross join 
-- method 1
select * from "students" , "payments" where id='22S001';

select * from "students" 
cross join "payments" ;


left join 
---------

select * from "students" as s
inner join "payments"  p
on s.id = p.student

-----
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    role VARCHAR(50),
    manager_id INT
);

-- drop table demo.employees;

INSERT INTO employees VALUES
(1, 'Arun', 'CEO', NULL),
(2, 'Bala', 'CTO', 1),
(3, 'Charan', 'HR Manager', 1),
(4, 'Divya', 'Team Lead', 2),
(5, 'Ezhil', 'Python Developer', 4),
(6, 'Farah', 'Python Developer', 4),
(7, 'Gokul', 'HR Executive', 3),
(8, 'Hari', 'Data Analyst', 2),
(9, 'Isha', 'Data Engineer', 2),
(10, 'Jeeva', 'Junior Developer', 5);
----------------

select * from employees;

select e2.emp_name,e2.role,e1.emp_name,e1.role
from employees as e1
join employees as e2 
on e1.emp_id = e2.manager_id

select * from customers;
select * from orders;


select * from students;
select * from courses;
select * from  payments;


select s.name,s.city,p.transaction_id,c.name,c.fee,p.paid
from students as s 
join payments as p 
on s.id = p.student 
join courses as c 
on p.course = c.id














select * from public.order;
select * from public.products;



