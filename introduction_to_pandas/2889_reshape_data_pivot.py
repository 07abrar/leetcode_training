import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index='month', columns='city', values='temperature')

if __name__ == "__main__":
    data = {
        'city': [
            'Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville',
            'ElPaso', 'ElPaso', 'ElPaso', 'ElPaso', 'ElPaso'
        ],
        'month': [
            'January', 'February', 'March', 'April', 'May',
            'January', 'February', 'March', 'April', 'May'
        ],
        'temperature': [13, 23, 38, 5, 34, 20, 6, 26, 2, 43]
    }
    weather = pd.DataFrame(data)
    print(pivotTable(weather))