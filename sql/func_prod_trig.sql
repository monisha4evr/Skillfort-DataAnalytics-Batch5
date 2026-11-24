select * from demo.employees_corr;

-- SQL Function
	-- reusable block of sql statements - to perform specific tasks and returns a result

Syntax:

CREATE OR REPLACE FUNCTION function_name( variable data_type)
RETURNS data_type 
LANGUAGE plpgsql
AS $$
BEGIN 
	-- sql statement 
	RETURN value;
END;
$$;

-- 

CREATE OR REPLACE FUNCTION demo.add_numbers()
RETURNS INT 
LANGUAGE plpgsql
AS $$
BEGIN 
	-- sql statement 
	RETURN 10+50;
END;
$$; 

select * from demo.add_numbers();


CREATE OR REPLACE FUNCTION demo.square_num(s_num INT)
RETURNS INT 
LANGUAGE plpgsql
AS $$
BEGIN 
	-- sql statement 
	RETURN s_num*s_num;
END;
$$; 

select * from demo.square_num(5);



CREATE OR REPLACE FUNCTION demo.get_emp_salary(pemp_id INT)
RETURNS INT 
LANGUAGE plpgsql
AS $$
DECLARE 
	emp_sal int;
BEGIN 
	return (
		select salary into emp_sal from demo.employees_corr where emp_id =pemp_id
	)

	-- select salary into emp_sal from demo.employees_corr where emp_id =pemp_id;
	-- RETURN emp_sal;
	-- RETURN emp_sal *5;
END;
$$; 

select * from demo.get_emp_salary(5);


CREATE OR REPLACE FUNCTION demo.get_empgreater_sal(amt INT)
RETURNS  TABLE(
	employee_name VARCHAR,
	employee_salary int
)
LANGUAGE plpgsql
AS $$
BEGIN 
	return query
	select emp_name,salary 
	from demo.employees_corr 
	where salary>amt;
END;
$$;

select * from demo.get_empgreater_sal(45000);


Procedure: 
- reusable block of code 
- insert , update, delete 
- precompiled query stored in database server 


CREATE OR REPLACE PROCEDURE procedure_name( parameter_name datatype)
LANGUAGE plpgsql
AS $$ 
BEGIN 
	-- sql statement
END;
$$;

call procedure_name(argument);


CREATE OR REPLACE PROCEDURE demo.get_employee_det(pemp_id INT)
LANGUAGE plpgsql
AS $$
DECLARE
    emp_rec RECORD;
BEGIN
    SELECT * INTO emp_rec 
    FROM demo.employees_corr 
    WHERE emp_id = pemp_id;

    RAISE NOTICE 'Employee Details: %', emp_rec;
END;
$$;

-- Run it with SELECT instead of CALL
call demo.get_employee_det(1);

SELECT * FROM demo.employees_corr where emp_id=1;


CREATE OR REPLACE PROCEDURE demo.update_salary(
IN p_emp_id INT,
IN p_sal INT)
LANGUAGE plpgsql
AS $$

BEGIN
	

END;
$$;update demo.employees_corr set salary=salary+p_sal
	where emp_id = p_emp_id;

call demo.update_salary(3,500);


CREATE OR REPLACE PROCEDURE demo.get_emp_sal(
IN p_emp_id INT,
out p_sal INT)
LANGUAGE plpgsql
AS $$
BEGIN
	select salary into p_sal from demo.employees_corr
	where emp_id=p_emp_id;
END;
$$;
call demo.get_emp_sal(1,null); 


CREATE OR REPLACE PROCEDURE demo.prd_inout_ex(
inout p_variab int)
LANGUAGE plpgsql
AS $$
BEGIN
	select salary into p_variab from demo.employees_corr
	where emp_id=p_variab;
END;
$$;
call demo.prd_inout_ex(3); 



CREATE OR REPLACE PROCEDURE demo.add_bonus(
in p_emp_id int)
LANGUAGE plpgsql
AS $$
declare b_sal int;
BEGIN
	select salary into b_sal from demo.employees_corr
	where emp_id=p_emp_id;

	if not found then
		raise notice 'Employee not Found';
	elseif b_sal>=45000 then
		update demo.employees_corr set salary=salary+500
		where emp_id = p_emp_id; 
		raise notice 'Bonus Added';
	else
		update demo.employees_corr set salary=salary+100
		where emp_id = p_emp_id; 
		raise notice 'Small Bonus Added';
	end if;

END
$$;

call demo.add_bonus(1);


-- Trigger

create or replace function customer_aud_func()
returns Trigger 
language plpgsql 
as $$ 
BEGIN
	INSERT INTO sampl(id, name,mobile,status)
    VALUES (NEW.id, 'INSERT',90909,1);

    RETURN NEW; 
END;
$$;

create trigger sal_update_trigger
after update of name
on samp 
for each row
execute function customer_aud_func();


select * from sampl;
select * from samp;

update samp set name='siva' where id='101014';
update samp set mobile='8090999' where id='101014';



Syntax:
select column_name,
case 
	when cond1 then result1
	when cond2 then result 
	else result3
end as new_col
from table_name;

select* from demo.employees_corr;


select emp_id,emp_name,salary,
case 
	when salary>=50000 then 'High'
	when salary>=40000 then 'medium' 
	else 'low'
end as Sal_band
from demo.employees_corr;

select * from demo.employees_corr where salary is null;
select emp_id,emp_name,coalesce(salary,0) as salary from  demo.employees_corr;


select nullif(10,10);
select nullif(10,20);

select col1 from table1 
union
select col1 from table2 

select col1 from table1 
union all
select col1 from table2 



-- windows function 
-- perform calculation across set of table rows that are related to current row
-- dont combine into single row 
-- Syntax:
-- over() sequence 

select col1,col2, window_function()
over(
	partition by col1
	order by col1
	rows/range between .. and .. -- window frame
) as alias_name 
from table_name

window functions
1. ranking Function 
	-- Row_number() - serial number
	-- rank() - gap  (1 2 2 4 5 5 7 )
	-- dense_rank() - no gap (1 2 2 3 4 5 5 6 7 )

2. aggregate function 
	-- min()
	-- max()
	-- sum()
	-- avg()
	-- count()

3. value/navigation 
	- lag
	- lead
	- first_value
	- last value
	- ntile ()

over()

select * from demo.employees_corr;
select count(*) from demo.employees_corr where dept_id=20;

select dept_id,avg(salary) as sal from demo.employees_corr group by dept_id

select emp_id,emp_name,dept_id,salary,
avg(salary) over() from demo.employees_corr;

select emp_id,emp_name,dept_id,salary,
avg(salary) over(
partition by dept_id
) from demo.employees_corr;



select emp_id,emp_name,dept_id,salary,
avg(salary) over(
partition by dept_id
-- order by dept_id asc,salary desc
),
count(emp_id) over(partition by dept_id),
min(salary) over (partition by dept_id),
sum(salary) over (partition by dept_id)
from demo.employees_corr;


select emp_id,emp_name,salary,dept_id,row_number() 
over(
order by salary desc
) as Row_no
from demo.employees_corr;

-- row_number + partition + order by (Doubt)
select emp_id,emp_name,salary,dept_id,row_number() 
over(
	partition by dept_id
) as Row_no
from demo.employees_corr;


-- Rank()

select emp_id,emp_name,salary,dept_id,rank() 
over(
	order by salary desc
) as Row_no
from demo.employees_corr;

-- dense rank()
select emp_id,emp_name,salary,dept_id,dense_rank() 
over(
	order by salary desc
) as Row_no
from demo.employees_corr;

select * from (
	select emp_id,emp_name,salary,dept_id,row_number() 
	over(
		partition by dept_id
		order by salary desc
	) as Row_no
	from demo.employees_corr
) as rn
where Row_no<=3
;



select  emp_id,emp_name,salary,dept_id,
lag(salary) over (
order by salary asc
) as previous_sal
from demo.employees_corr;


select  emp_id,emp_name,dept_id,salary,
lag(salary) over (
partition by dept_id 
order by salary asc
) as previous_sal
from demo.employees_corr;

select  emp_id,emp_name,dept_id,salary,
lag(salary) over (
partition by dept_id 
order by salary asc
) as previous_sal,
salary - lag(salary) over (
partition by dept_id 
order by salary asc
) as difference
from demo.employees_corr;



SELECT 
    emp_id,
    emp_name,
    dept_id,
    salary,
    LAG(salary) OVER w AS previous_sal,
    salary - LAG(salary) OVER w AS difference
FROM demo.employees_corr
WINDOW w AS (PARTITION BY dept_id ORDER BY salary ASC);

select  emp_id,emp_name,dept_id,salary,
lead(salary) over (
partition by dept_id 
order by salary asc
) as nex_sal
from demo.employees_corr;


select  emp_id,emp_name,dept_id,salary,
lead(salary) over (
partition by dept_id 
order by salary desc
) as nex_sal
from demo.employees_corr;

-- first value 

select emp_name,dept_id,salary,
first_value(emp_name)
over(
	partition by dept_id
	order by salary desc,emp_id
) as higest_paid_emplyee
from demo.employees_corr;


select emp_name,dept_id,salary,
first_value(emp_name)
over(
	partition by dept_id
	order by salary desc
) as higest_paid_emplyee
from demo.employees_corr;


select emp_name,dept_id,salary,
first_value(salary)
over(
	partition by dept_id
	order by salary asc
) as lowest_paid_emplyee
from demo.employees_corr;


select emp_name,dept_id,salary,
first_value(salary)
over(
	partition by dept_id
	order by salary desc
) as lowest_paid_emplyee
from demo.employees_corr;




-- frame types;

current row 
preceding (previous row)
following 
unbounded 


1. previous rows to current row 

rows between unbounded preceding and current row  

2. current row + next row 

rows between current row and 1 following 

3. current row + 1 previous row 

rows between 1 preceding row and current row 

4. entire partition 

rows between unbounded preceding and unbounded following 


select emp_name,dept_id,salary,
last_value(salary)
over(
	partition by dept_id
	order by salary asc
	rows between unbounded preceding and unbounded following
) as lowest_paid_emplyee
from demo.employees_corr;







