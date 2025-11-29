
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    birth_year INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    subject TEXT NOT NULL,
    grade INTEGER NOT NULL CHECK (grade >= 1 AND grade <= 100),
    FOREIGN KEY (student_id) REFERENCES students (id)
);

INSERT INTO students (full_name, birth_year) VALUES
('Alice Johnson', 2005),
('Brian Smith', 2004),
('Carla Reyes', 2006),
('Daniel Kim', 2005),
('Eva Thompson', 2003);

INSERT INTO grades (student_id, subject, grade) VALUES
(1, 'Math', 88),
(1, 'English', 92),
(1, 'Science', 85),
(2, 'Math', 75),
(2, 'History', 83),
(2, 'English', 79),
(3, 'Science', 95),
(3, 'Math', 91),
(3, 'Art', 89),
(4, 'Science', 88),
(4, 'Physical Education', 93),
(4, 'Math', 84),
(5, 'English', 90),
(5, 'History', 85),
(5, 'Math', 88);

SELECT s.full_name, g.subject, g.grade
FROM grades g
JOIN students s ON g.student_id = s.id
WHERE s.full_name = 'Alice Johnson';

-- 4. Средняя оценка для каждого студента
SELECT s.full_name, ROUND(AVG(g.grade), 2) as average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id, s.full_name;

-- 5. Студенты, родившиеся после 2004 года
SELECT full_name, birth_year
FROM students
WHERE birth_year > 2004;

-- 6. Средние оценки по предметам
SELECT subject, ROUND(AVG(grade), 2) as average_grade
FROM grades
GROUP BY subject;

-- 7. Топ-3 студентов с самыми высокими средними оценками
SELECT s.full_name, ROUND(AVG(g.grade), 2) as average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id, s.full_name
ORDER BY average_grade
LIMIT 3;

-- 8. Студенты с оценками ниже 8
SELECT s.full_name, g.subject, g.grade
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.grade < 80;