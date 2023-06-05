# -*- coding: utf-8 -*-
"""Demographics Data Analysis Using Pandas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nP7bkeYwuvS5nle5ZMKXLpnLHrGPeT-3
"""

import pandas as pd

#Read CSV file
dataset = pd.read_csv('/content/adult.data.csv')
print(dataset)

#Count of people of each race
race_counts = dataset['race'].value_counts()
print("Number of people of each race:")
print(race_counts)

#Average age of men
average_age_men = dataset.loc[dataset['sex'] == 'Male', 'age'].mean()
print("Average age of men:", round(average_age_men, 2))

#Percentage of people with a Bachelor's degree
percentage_bachelors = (dataset['education'] == 'Bachelors').mean() * 100
print("Percentage of people with a Bachelor's degree:", round(percentage_bachelors, 2))

#Percentage of people with advanced education making more than 50K
advanced_education = dataset['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
percentage_advanced_education = (dataset.loc[advanced_education, 'salary'] == '>50K').mean() * 100
print("Percentage of people with advanced education making more than 50K:", round(percentage_advanced_education, 2))

#Percentage of people without advanced education making more than 50K
no_advanced_education = ~advanced_education
percentage_no_advanced_education = (dataset.loc[no_advanced_education, 'salary'] == '>50K').mean() * 100
print("Percentage of people without advanced education making more than 50K:", round(percentage_no_advanced_education, 2))

#Minimum number of hours a person works per week
min_hours_per_week = dataset['hours-per-week'].min()
print("Minimum number of hours a person works per week:", min_hours_per_week)

#Percentage of people who work the minimum hours per week and have salary >50K
min_hours_50k = (dataset.loc[dataset['hours-per-week'] == min_hours_per_week, 'salary'] == '>50K').mean() * 100
print("Percentage of people who work the minimum hours per week and have salary >50K:", round(min_hours_50k, 2))

#Country with the highest percentage of people earning >50K and the percentage
country_highest_50k = dataset.loc[dataset['salary'] == '>50K', 'native-country'].value_counts(normalize=True).idxmax()
percentage_highest_50k = (dataset.loc[dataset['native-country'] == country_highest_50k, 'salary'] == '>50K').mean() * 100
print("Country with the highest percentage of people earning >50K:", country_highest_50k)
print("Percentage of people earning >50K in that country:", round(percentage_highest_50k, 2))

#Most popular occupation for those earning >50K in India
india_high_income_occupation = dataset.loc[(dataset['native-country'] == 'India') & (dataset['salary'] == '>50K'), 'occupation'].value_counts().idxmax()
print("Most popular occupation for those earning >50K in India:", india_high_income_occupation)