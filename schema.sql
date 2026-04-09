-- file used to hold sql commands

--exercise table to hold info about each exercise
CREATE TABLE IF NOT EXISTS exercise(
    exercise_id INT,
    exercise_name VARCHAR(50),
    muscle_group VARCHAR(20)
);
CREATE TABLE IF NOT EXISTS workout(
    workout_id INT,
    workout_date DATE
);
CREATE TABLE IF NOT EXISTS set(
    set_id INT,
    workout_id INT,
    exercise_id INT,
    weight_lb INT,
    reps INT
);