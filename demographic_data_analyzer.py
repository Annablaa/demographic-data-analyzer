import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")
  
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = (df[df['sex']=='Male'])['age'].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    total_count_people = df.shape[0]
    people_bachelor = (df[df["education"] == 'Bachelors']).shape[0]
    percentage_bachelors = round(people_bachelor/total_count_people * 100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    advanced_education_levels = ['Bachelors', 'Masters', 'Doctorate']
    filtered_df = df[df['education'].isin(advanced_education_levels)]
    # What percentage of people without advanced education make more than 50K?
    non_advanced = df[~df['education'].isin(advanced_education_levels)]
   
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = filtered_df[filtered_df['salary'] == '>50K']
    lower_education = non_advanced[non_advanced['salary'] == '>50K']

    # percentage with salary >50K
    higher_education_rich = round((higher_education.shape[0] / filtered_df.shape[0]) * 100,1)
    lower_education_rich = round((lower_education.shape[0] / non_advanced.shape[0]) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers = num_min_workers[num_min_workers['salary'] == '>50K']
    rich_percentage = round((rich_min_workers.shape[0]/num_min_workers.shape[0]) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    country_income_percentage = df.groupby('native-country')['salary'].apply(lambda x: (x == '>50K').mean() * 100)
    highest_earning_country = country_income_percentage.idxmax()
    highest_earning_country_percentage = round(country_income_percentage.max(),1)

    # Identify the most popular occupation for those who earn >50K in India.
    india_high_income = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_high_income['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
