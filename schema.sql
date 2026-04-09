-- file used to hold sql commands
--exercise table to hold info about each exercise
CREATE TABLE IF NOT EXISTS users(
    user_id INT,
    user_name VARCHAR(20)
);
CREATE TABLE IF NOT EXISTS exercises(
    exercise_id INT PRIMARY KEY,
    exercise_name VARCHAR(50) NOT NULL,
    primary_muscle_group VARCHAR(20)
);
CREATE TABLE IF NOT EXISTS workouts(
    workout_id INT PRIMARY KEY,
    workout_date DATE,
    user_id INT,
    note VARCHAR(500)
);
CREATE TABLE IF NOT EXISTS workout_exercises(
    workout_exercise_id INT PRIMARY KEY,
    workout_id INT,
    exercise_id INT
);
CREATE TABLE IF NOT EXISTS sets_info(
    set_id INT PRIMARY KEY,
    workout_exercise_id INT,
    set_number INT,
    weight_lb DECIMAL,
    reps INT
);