# Project: Demographic Data Analysis

This project is part of the **freeCodeCamp Data Analysis with Python** course. The goal is to analyze demographic data extracted from the 1994 Census database using Pandas and answer specific questions regarding race representation, education levels, salary distribution, and work hours.

## Project Overview

We will use Pandas to process and analyze the dataset. The dataset includes information such as age, race, education, occupation, and salary, and we will answer several demographic questions.

### Key Questions:
1. How many people of each race are represented in the dataset?
2. What is the average age of men?
3. What percentage of people have a Bachelor's degree?
4. What percentage of people with advanced education (Bachelors, Masters, Doctorate) make more than 50K?
5. What percentage of people without advanced education make more than 50K?
6. What is the minimum number of hours a person works per week?
7. What percentage of people who work the minimum number of hours per week have a salary of more than 50K?
8. Which country has the highest percentage of people earning more than 50K?
9. What is the most popular occupation for people earning more than 50K in India?

## Requirements

You need the following libraries to run this project:
- **Pandas**: For data manipulation and analysis.
- **NumPy**: To facilitate numerical operations.

You can install the required libraries using pip:

```bash
pip install pandas numpy
```

## Files
- **demographic_data.csv**: The dataset extracted from the 1994 Census database.

## Code Overview

### Data Preprocessing
1. **Loading the Data**: The dataset is loaded using `pd.read_csv()`.

2. **Calculating Race Representation**: 
- The count of people in each race category is determined using `value_counts()` on the race column.

3. **Average Age of Men**: 
- The average age of men is calculated by filtering the dataset for rows where `sex == 'Male'` and calculating the mean of the `age` column.

4. **Percentage of People with a Bachelor's Degree**:
- The percentage of people holding a Bachelor's degree is determined by dividing the count of rows with `education == 'Bachelors'` by the total number of rows.

5. **Advanced Education and Salary**:
- The percentage of people with advanced education (Bachelors, Masters, Doctorate) earning more than 50K is calculated by filtering the dataset for the respective degrees and counting the number of people with a salary greater than 50K.

6. **Minimum Hours Worked and Salary**:
- The minimum number of hours worked per week is determined using the `min()` function on the `hours-per-week` column. Then, we calculate the percentage of people working the minimum hours and earning more than 50K.

7. **Country with Highest Percentage of People Earning >50K**:
- We calculate the percentage of people in each country earning more than 50K by dividing the number of people earning more than 50K by the total number of people from that country. The country with the highest percentage is identified.

8. **Most Popular Occupation for High Earners in India**:
- The most common occupation for people earning more than 50K in India is determined using the `mode()` function.

## How to Run

1. Clone this repository to your local machine.
2. Install the required libraries using the commands provided.
3. Ensure the dataset file (`demographic_data.csv`) is in the same directory as the script.
4. Run the Python script:
```bash
python demographic_data_analyzer.py
```
5. The results will be printed to the console.

## Conclusion
This project uses Pandas to effectively analyze a large dataset and answer demographic questions. It provides insights into the relationships between education, salary, work hours, and other variables based on 1994 Census data.
