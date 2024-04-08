import pandas as pd
def main():
    excel_path = "data.xlsx"
    df = pd.read_excel(excel_path)
    cleaned_df = clean_dataframe(df)
    cleaned_excel_path = "cleaned_data.xlsx"
    cleaned_df.to_excel(cleaned_excel_path, index=False)
    print("Cleaned data has been exported to", cleaned_excel_path)

if __name__ == "main":
    main()
def clean_special_characters(text):
    if isinstance(text, str):  
        return ''.join(e for e in text if e.isalnum() or e.isspace())
    else:
        return str(text)  

def clean_dataframe(df):
    cleaned_df = df.applymap(clean_special_characters)
    cleaned_df.drop_duplicates(inplace=True)
    return cleaned_df
