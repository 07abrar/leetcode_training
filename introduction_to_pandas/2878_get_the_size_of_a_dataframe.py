import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> list[int]:
    return [players.shape[0], players.shape[1]]


if __name__ == "__main__":
    data = {'player_id': [846, 749, 155],
        'name': ['Mason', 'Riley', 'Bob'],
        'age': [21, 30, 28],
        'position': ['Forward', 'Winger', 'Striker']
    }
    players = pd.DataFrame(data)
    print(getDataframeSize(players))

    data = {
        'player_id': [846, 749, 155, 583, 388, 883, 355, 247, 761, 642],
        'name': [
            'Mason', 'Riley', 'Bob', 'Isabella', 'Zachary',
            'Ava', 'Violet', 'Thomas', 'Jack', 'Charlie'
        ],
        'age': [21, 30, 28, 32, 24, 23, 18, 27, 33, 36],
        'position': [
            'Forward', 'Winger', 'Striker', 'Goalkeeper', 'Midfielder',
            'Defender', 'Striker', 'Striker', 'Midfielder', 'Center-back'
        ],
        'team': [
            'RealMadrid', 'Barcelona', 'ManchesterUnited', 'Liverpool',
            'BayernMunich', 'Chelsea', 'Juventus', 'ParisSaint-Germain',
            'ManchesterCity', 'Arsenal'
        ]
    }
    players = pd.DataFrame(data)
    print(getDataframeSize(players))