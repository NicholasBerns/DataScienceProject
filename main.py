import pandas
import pandas as pd

while True:
    selection = input("Load MTurk or Toloka data (M/T): ")
    if selection == "M":
        df = pd.read_csv("data/records.csv",
                         names=['ID', 'Current', 'Event', 'Extra', 'Platform', 'Skip', 'Subtype', 'Time', 'Type',
                                'User'])
        break
    elif selection == "T":
        df = pd.read_csv("data/telemetry_db.csv")
        df.drop(0)
        df.columns = ['ID', 'Current', 'Event', 'Extra', 'Platform', 'Skip', 'Subtype', 'Time', 'Type', 'User',
                      'Irrelevant', 'Unused']
        df = df.drop(columns=['Irrelevant', 'Unused'])
        break
    else:
        print("Invalid Selection")

# ID =
print(df.head(), end="\n\n")
print(df.info(), end="\n\n")
print(df.columns)
