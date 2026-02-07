import pandas as pd

# 1. Load the original Excel file
file_path = 'Python_Books_Library.xlsx'
df = pd.read_excel(file_path)

# 2. Create a new DataFrame for the final output
df_final = pd.DataFrame()

# 3. Process the first column (Book Title) by splitting at the ':' character
# This creates the 'Book Name' and 'Description' columns
split_data = df.iloc[:, 0].astype(str).str.split(':', n=1, expand=True)

# Fill 'Book Name' (everything before the colon)
df_final['Book Name'] = split_data[0].str.strip()

# Fill 'Description' (everything after the colon, if it exists)
if 1 in split_data.columns:
    df_final['Description'] = split_data[1].str.strip().fillna("")
else:
    df_final['Description'] = ""

# 4. Add the 'Author' column from the second column of the original file
if df.shape[1] > 1:
    df_final['Author'] = df.iloc[:, 1].astype(str).str.strip()
else:
    df_final['Author'] = ""

# 5. Save the cleaned data to a new Excel file
output_file = 'Final_Python_Books_Library.xlsx'
df_final.to_excel(output_file, index=False)

print(f"✅ Code successfully executed with 3 columns. Created: '{output_file}'")