-- subquery
-- query written inside another query 
-- outer query -> written outside 
-- inner query -> written Inside 

types 
1. correlation subquery ( inner query  expect outer quter to execute )  exists , in , any
2. non correlation subquery  ( inner query run independently )

2. non correlation subquery  ( inner query run independently )
	1. scalar/single row subquery - (comparision operation)
	2. derived/inline multiple row subquery
	3. multiple column subquery

Subquery => ()
-- where we can add subquery
select clause 
from clause 
where clause 
having clause 


select * from public.orders;

select avg(total_amount) from public.orders; 

select * from public.orders where total_amount>='7804';

-- single row sub query
select * from public.orders where total_amount<(select avg(total_amount) from public.orders)
-- multiple row sub query

select * from public.products;






