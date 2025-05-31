import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'] * 2
    return employees

if __name__ == "__main__":
    data = {
        'name': ['Jack', 'Piper', 'Mia', 'Ulysses'],
        'salary': [19666, 74754, 62509, 54866]
    }
    employees = pd.DataFrame(data)
    print(modifySalaryColumn(employees))