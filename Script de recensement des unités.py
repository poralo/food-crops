import pandas

dataframe = pandas.read_csv("FeedGrains.csv")

UnitList = []

for index, row in dataframe.iterrows():
    column_value = (row['SC_Unit_Desc'], row['SC_Unit_ID'])
    if column_value not in UnitList:
        UnitList.append(column_value)
print(UnitList)

