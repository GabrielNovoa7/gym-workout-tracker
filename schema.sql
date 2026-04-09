-- file used to hold sql commands

--exercise table to hold info about each exercise
CREATE TABLE IF NOT EXISTS exercises(
    exercise_id INT PRIMARY KEY,
    exercise_name VARCHAR(50) NOT NULL,
    muscle_group VARCHAR(20)
);
CREATE TABLE IF NOT EXISTS workouts(
    workout_id INT PRIMARY KEY,
    workout_date DATE
);
CREATE TABLE IF NOT EXISTS set_info(
    set_id INT PRIMARY KEY,
    workout_id INT,
    exercise_id INT,
    weight_lb INT,
    reps INT NOT NULL 
);