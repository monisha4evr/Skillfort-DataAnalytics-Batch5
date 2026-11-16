SELECT emp_name, salary,dept_id
FROM demo.employees_corr
WHERE salary IN (
    SELECT salary
    FROM demo.employees_corr
    WHERE dept_id = 10
)
ORDER BY salary,dept_i;