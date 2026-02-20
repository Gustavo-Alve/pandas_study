import pandas as pd

#see what gender is more popular
#famouse divice type (ANDROID OR IOS)
#who stay more time at the social medias
df =pd.read_csv('Smartphone_Usage_Productivity_Dataset_50000.csv')

count = df['Gender']
print(count.type())