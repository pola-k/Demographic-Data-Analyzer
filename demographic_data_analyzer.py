import numpy as np
import pandas as pd


def analyse():
    census = pd.read_csv("demographic_data.csv")

    race = census['race'].value_counts().tolist()
    print(race)

    condition = census['sex'] == 'Male'
    men_avg_age = round(census.loc[condition, 'age'].mean().tolist(), 1)
    print(men_avg_age)

    total_data_size = len(census)
    condition2 = census['education'] == 'Bachelors'
    people_with_bachelors = len(census.loc[condition2])
    percentage_of_people_with_bachelors = round((people_with_bachelors / total_data_size) * 100, 1)
    print(percentage_of_people_with_bachelors)

    condition3 = census['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    condition4 = census['salary'] == '>50K'
    advance_education = len(census.loc[condition3])
    advance_education_salary = len(census.loc[condition3 & condition4])
    percentage_of_people_with_advance_education_salary = round((advance_education_salary / advance_education) * 100, 1)
    print(percentage_of_people_with_advance_education_salary)

    without_advance_education = len(census.loc[(census['education'] != 'Bachelors') & (census['education'] != 'Masters') & (census['education'] != 'Doctorate')])
    without_advance_education_salary = len(census.loc[(census['education'] != 'Bachelors') & (census['education'] != 'Masters') & (census['education'] != 'Doctorate') & condition4])
    percentage_of_people_without_advance_education_salary = round((without_advance_education_salary / without_advance_education) * 100, 1)
    print(percentage_of_people_without_advance_education_salary)

    minimum_hours = census['hours-per-week'].min().tolist()
    print(minimum_hours)

    condition5 = census['hours-per-week'] == minimum_hours
    work_min_hours = len(census.loc[condition5])
    people_working_min_salary = len(census.loc[condition5 & condition4])
    percentage_of_people_working_min_salary = round((people_working_min_salary / work_min_hours) * 100, 1)
    print(percentage_of_people_working_min_salary)

    data = census.loc[condition4, 'native-country'].value_counts() / census['native-country'].value_counts()
    data.sort_values(ascending=False, inplace=True)
    p = data.iloc[0]
    rich_percentage = round(p * 100, 1)
    country = data[data == data.max()].index[0]
    print(country)
    print(rich_percentage)

    condition7 = census['native-country'] == 'India'
    india_fav_occupation = census.loc[condition7 & condition4, 'occupation'].mode().tolist()[0]
    print(india_fav_occupation)

    return None


analyse()
