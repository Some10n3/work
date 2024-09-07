%Facts in reg_sys

% student(student, year, program)
student(tin, 3, se).
student(sugar, 4, me).
student(matt, 2, fe).

% course(course, year, program)
course(cs101, 3, se).
course(cs102, 3, se).
course(cs103, 2, fe).

% completed(student, course)
completed(tin, cs101).
completed(sugar, cs102).
completed(matt, cs103).

% required(courseA, courseB)
% courseA requires courseB as a prerequisite
required(cs102, cs101).
required(cs103, cs102).

%Rule in reg_sys

% can_enroll(Student, Course) succeeds if Student can enroll in Course
can_enroll(Student, Course) :-
    student(Student, Year, Program),
    course(Course, Year, Program),
    \+ completed(Student, Course),
    required_for_course(Course, RequiredCourses),
    check_required_courses(RequiredCourses, Student).

% Helper predicate to find all required courses for a given course
required_for_course(Course, RequiredCourses) :-
    findall(R, required(Course, R), RequiredCourses).

% Helper predicate to check if all required courses for a course are completed by a student
check_required_courses([], _). % Base case: no required courses means all requirements are met
check_required_courses([Course|Remaining], Student) :-
    completed(Student, Course), % Check if the student has completed the current required course
    check_required_courses(Remaining, Student). % Recursively check the remaining required courses

classmates(Student1, Student2) :-
    student(Student1, Year, Program),
    student(Student2, Year, Program),
    Student1 \= Student2.