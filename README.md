# Magpie Literacy

## Overview

This is a simple web application that allows users to visualize the proficiency of different skills.

## Getting Started
### 1. Install Python Poetry
Python poetry is a modern dependency management and packaging tool for Python, aiming to simplify the process of library development and publication. Below are the steps to install Poetry on your system.

1. Ensure that Python is installed on your system. Python3.12 is required for the project.
2. poetry provides an installer script that can be executed to install the latest version. Run the following command in your terminal (try python instead of python3 if it errors):
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

3. To install dependencies, you will need to run the following command in your code editor:
```bash
poetry install
```
(Make sure that your filepath in your terminal is within the poetry project subfolder `magpie`)

### 2. Run the application
To run the application, you'll need to make sure that you are in your terminal. You should be able to
run the following command:
```bash
poetry run streamlit run magpie/main.py
```

In the terminal output, there should be printed the question and answers for question 1 and 2. Question 3 (visualization) will open a new browser tab automatically as a Streamlit app to be interfaced with.

### Exiting the Application
You can exit the application by simply pressing the `Ctrl+C` key combination in your terminal.

## Notes
* The application allows you to view the skill report in 3 different ways:
    * Bar chart
        - Two bar charts showing the record counts of each skill level as well as the average proficiency for each skill level.
    * Dual axis chart
        - A dual axis chart showing the record counts of each skill level as well as the average proficiency for each skill level.
        - Note: the averages for each skill are seen on the right y-axis; the left y-axis shows the record counts.
    * Side by side chart
        - A side by side chart showing the record counts of each skill level as well as the average proficiency for each skill level.
    * Sample images of these can be seen in the `magpie/sample{n}.png` files.
* The application also allows you to upload your own data to view in the skill reports, although this defaults to the one derived from the sample data.
* Although the question 2 asks for proficiency.json and skill.json consumption, it does not appear that these are used at all in the application.
