import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students

if __name__ == "__main__":
    data = {
        'student_id': [1, 2],
        'name': ['Ava', 'Kate'],
        'age': [6, 15],
        'grade': [73.0, 87.0]
    }
    students = pd.DataFrame(data)
    print(changeDatatype(students))