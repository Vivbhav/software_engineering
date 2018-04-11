CREATE TABLE events_list (
	event_id INT PRIMARY KEY AUTO_INCREMENT,
	event_name VARCHAR(50),
	start_time VARCHAR(50),
	end_time VARCHAR(50)
);

CREATE TABLE tasks (
	task_id INT PRIMARY KEY AUTO_INCREMENT,
	task_name VARCHAR(50), 
	duration INT
);
