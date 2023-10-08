USE estate;

SELECT * FROM apartment;

select count(id) from apartment;

select count(id) from apartment
where overall_price IS NOT NULL;