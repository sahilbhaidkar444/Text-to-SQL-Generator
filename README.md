# Text to SQL Generator

This project utilizes Google's Generative AI API and Streamlit to create a user-friendly interface for generating SQL queries based on natural language input. It assists users who may not be familiar with SQL syntax to interact with databases seamlessly.

## Features

- **Natural Language Processing**: Leveraging Google's Generative AI API for understanding user queries in natural language.
- **Interactive Web Interface**: Utilizing Streamlit to create an interactive web application for user interaction.
- **SQL Query Generation**: Automatically generates SQL queries based on user input.
- **Static Database**: Utilizes a static database generated within the application.
- **Anime Database**: The provided database contains information about anime.
- **Data Display**: The application displays the data in the database based on user queries.
- **Easy Deployment**: Streamlit allows for simple deployment of the application.

## Libraries Used

- **Streamlit**: For creating the interactive web application.
- **Google's Generative AI API**: For natural language processing to understand user queries.
- **sqlite3**: For interacting with SQLite databases.
- **dotenv**: For loading environment variables from a .env file.

## Getting Started

To get started with the Text to SQL Project with a static anime database, follow these steps:

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/sahilbhaidkar444/Text-to-SQL-Generator.git
    ```

2. Install the necessary dependencies. Make sure you have Python installed on your system. You can install dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit application for the static anime database:

    ```bash
    streamlit run app.py
    ```

4. Open your web browser and navigate to the URL provided by Streamlit to access the Text to SQL interface.

## Usage

1. Enter your query in natural language.
2. Click the "Generate SQL" button.
3. The application will process your query and display the corresponding SQL query.
4. Optionally, you can copy the generated SQL query and execute it on your database.
5. The application will also display the data in the database based on the generated SQL query.

## Example

**Input**: "Show me all the anime with a rating above 8."

**Output**: 
```sql
SELECT * FROM anime WHERE rating > 8;


| id |       title        | episodes | rating |
|----|--------------------|----------|--------|
| 1  | Death Note         | 37       | 9.0    |
| 2  | Attack on Titan    | 59       | 8.5    |
| 3  | Fullmetal Alchemist| 64       | 9.1    |

```
# Contributions

Contributions are welcome! If you would like to contribute to this project, feel free to submit a pull request.
