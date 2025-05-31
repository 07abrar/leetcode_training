import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=['name'])

if __name__ == "__main__":
    data = {
        'student_id': [32, 217, 779, 849],
        'name': ['Piper', None, 'Georgia', 'Willow'],
        'age': [5, 19, 20, 14]
    }
    students = pd.DataFrame(data)
    print(dropMissingData(students))