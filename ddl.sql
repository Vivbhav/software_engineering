CREATE TABLE events (
	event_id INT PRIMARY KEY AUTO_INCREMENT,
	event_name VARCHAR(50),
	start_time datetime,
	end_time datetime
);

CREATE TABLE tasks (
	task_id INT PRIMARY KEY AUTO_INCREMENT,
	task_name VARCHAR(50), 
	duration INT
);
