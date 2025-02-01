def gradingStudents(grades):
    final_grades = []
    for grade in grades:
        if grade < 38:
            final_grades.append(grade)      
        else:
            difference = 5 - (grade % 5)
            if difference < 3:
                final_grades.append(grade + difference)
            else:
                final_grades.append(grade)
    
    return final_grades