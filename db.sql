-- Create the table
create table things (
	thing text,
	entrytimestamp timestamptz
);

-- Add some dummy data for testing
insert into things (thing, entrytimestamp)
values
	('test', current_timestamp),
	('test', current_timestamp),
	('bob', current_timestamp),
	('dog', current_timestamp)

-- Verify the table looks correct
select * from things;

-- Test pulling records from last 1000 seconds and aggregating by word
select
	thing,
	count(thing)
from
	things
where
	entrytimestamp >= current_timestamp - interval '1000 seconds'
group by thing;

-- Clear the table
truncate table things;