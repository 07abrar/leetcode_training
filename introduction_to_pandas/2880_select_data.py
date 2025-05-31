import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    student = students[students['student_id'] == 101]
    return student[['name', 'age']]

if __name__ == "__main__":
    data = {
        'student_id': [101, 53, 128, 3],
        'name': ['Ulysses', 'William', 'Henry', 'Henry'],
        'age': [13, 10, 6, 11]
    }
    students = pd.DataFrame(data)
    print(selectData(students))