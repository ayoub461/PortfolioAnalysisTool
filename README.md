Portfolio Analysis and Data Processing
This project is designed to perform portfolio analysis by reading stock data from CSV files, calculating daily returns, and computing the overall portfolio return. It uses Python along with pandas for data manipulation and analysis.

Project Structure
main.py: The main script to run the portfolio analysis.
p_Supportfunction.py: Contains support functions used in the main script.
Requirements
Python 3.x
pandas
You can install the required packages using pip:

sh
Copy code
pip install pandas
Usage
Ensure that your CSV files are in the Downloads directory and that each file contains a "Date" and an "Adj Close" column.
Run the main.py script.
sh
Copy code
python main.py
The script will prompt you to enter the number of elements (stocks) you want to include in your portfolio, the file names, and the respective weights for each stock.

Example CSV File Structure
Your CSV files should have the following structure:

csv
Copy code
Date,Adj Close
2023-01-01,100.5
2023-01-02,101.0
...
Functions
main.py
main(): The main function that orchestrates the data reading, cleaning, and analysis processes.
Reads the number of elements and file names.
Loads data from CSV files in the Downloads directory.
Cleans and formats the data.
Calculates daily returns for each stock.
Computes the overall portfolio return.
Saves the results to Portfolio_Analysis.csv.
p_Supportfunction.py
get_int_positive(prompt): Prompts the user to enter a positive integer.
get_int(prompt): Prompts the user to enter an integer.
get_float_positive(prompt): Prompts the user to enter a positive float or fraction.
get_percentage(prompt): Prompts the user to enter a percentage (value between 0 and 1).
Error Handling
The script includes error handling for:

File not found.
Missing or incorrect columns in the CSV files.
Date parsing errors.
Indexing and NaN value handling.
Output
The output is saved to Portfolio_Analysis.csv and includes the daily returns for each stock and the overall portfolio return.

Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request.
