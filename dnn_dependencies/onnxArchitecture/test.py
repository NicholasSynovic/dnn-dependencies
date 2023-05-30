from pandas import DataFrame
data = {
    'ID' : [0, 1, 2, 3, 4, 5, 6, 7],
    'Output' : ['test0', 'test1', 'test2', 'test3', 'test2', 'test5', 'test1', 'test7']
}



df = DataFrame(data)


data1 = {
    'Input' : ['input0', 'input1', 'input2', 'input3', 'input4', 'input5', 'input6', 'input7']
}

df['Input'] = data1['Input']

df_unique = df.drop_duplicates(subset=['Output'])

print(df_unique)


