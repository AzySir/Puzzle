

## Puzzle 1 - Count rows of a csv file
**Problem Statement:** This application takes all the rows inside of the csv-sample.csv file and creates a list then counts the row. The solution here to decrease from 1028  lines to 1024 is that the list took into consideration of the escaped special characters and decreased the row count by 4.

**Challenge:** The [csv-sample.csv](./csv-sample.csv) has 1024 rows and you can verify this by opening it in Excel. If you open the file using a plain text editor such as notepad, you will notice that it has 1028 lines. 

**Solution:** Python

**To Run Code:**

```
python3 custom_csv.py
```
