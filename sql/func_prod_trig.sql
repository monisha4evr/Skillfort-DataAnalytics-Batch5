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
