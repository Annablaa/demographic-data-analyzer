import pandas as pd

df = pd.read_csv("adult.data.csv")
print(df)
print(df.columns)
print(df['race'].value_counts())   #race represented
print(df['sex'].value_counts()['Male'])
print((df[df['sex']=='Male'])['age'].mean().round(1))
print((df[df["education"] == 'Bachelors']).shape[0])

total_count_people = df.shape[0]
people_bachelor = (df[df["education"] == 'Bachelors']).shape[0]
percentage_bachelors = round(people_bachelor/total_count_people * 100,1)
print(percentage_bachelors)
print(df['education'].unique())
print(df['hours-per-week'].min())
advanced_education_levels = ['Bachelors', 'Masters', 'Doctorate']
filtered_df = df[df['education'].isin(advanced_education_levels)]
filtered_income = filtered_df[filtered_df['salary'] == '>50K']
percentage_advanced_education = round((filtered_income.shape[0] / filtered_df.shape[0]) * 100,1)
higher_education = percentage_advanced_education

non_advanced = df[~df['education'].isin(advanced_education_levels)]
non_advanced_income = non_advanced[non_advanced['salary'] == '>50K']
percentage_nonadvanced = round((non_advanced_income.shape[0] / non_advanced.shape[0]) * 100, 1)
print(percentage_nonadvanced)

min_work_hours = df['hours-per-week'].min()
num_min_workers = df[df['hours-per-week'] == min_work_hours]
rich_min_workers = num_min_workers[num_min_workers['salary'] == '>50K']
rich_percentage = round((rich_min_workers.shape[0]/num_min_workers.shape[0]) * 100, 1)
print(rich_percentage)
print(df.columns)
print(df['native-country'])


# Grouping by native country and calculating the percentage of people earning >50K
country_income_percentage = df.groupby('native-country')['salary'].apply(lambda x: (x == '>50K').mean() * 100)

# Finding the country with the highest percentage
highest_earning_country = country_income_percentage.idxmax()
highest_earning_country_percentage = round(country_income_percentage.max(),1)

print("Country with the highest percentage of people earning >50K:", highest_earning_country)
print("Percentage:", highest_earning_country_percentage)

india_high_income = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
most_popular_occupation = india_high_income['occupation'].value_counts().idxmax()





