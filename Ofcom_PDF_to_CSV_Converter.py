import camelot
import pandas as pd
import re  # Import regular expressions for data cleaning

def extract_tables_from_pdf(pdf_path):
    # Extract tables from the PDF
    tables = camelot.read_pdf(pdf_path, pages='2-end')
    return tables

def process_table(tables):
    all_data = []
    for table in tables:
        # Convert table to DataFrame
        df = table.df
        
        # Print the DataFrame for debugging
        print("Original DataFrame:")
        print(df)
        
        # Extract numbers from column 1 starting from row 11
        if df.shape[0] > 1:
            df_filtered = df.iloc[1:, 1]  # Start from row 11, column 1
            
            # Clean and extract numeric values
            df_filtered = df_filtered.apply(lambda x: re.sub(r'[^\d.]+', '', x))  # Remove non-numeric characters except '.'
            df_filtered = pd.to_numeric(df_filtered, errors='coerce')  # Convert to numeric, NaNs will be produced for non-numeric values
            df_filtered = df_filtered.dropna()  # Drop NaNs
            
            # Print the cleaned data for debugging
            print("Cleaned DataFrame:")
            print(df_filtered)
            
            print("Extracted Numbers:")
            print(df_filtered)
            all_data.extend(df_filtered.tolist())
    
    return all_data

def save_to_csv(data, csv_path):
    # Convert data to DataFrame and save as CSV
    df = pd.DataFrame(data, columns=['Licensed Frequency'])
    df.to_csv(csv_path, index=False)
    print(f"Data saved to {csv_path}")

def main(pdf_path, csv_path):
    tables = extract_tables_from_pdf(pdf_path)
    all_data = process_table(tables)
    save_to_csv(all_data, csv_path)

# Example usage
if __name__ == "__main__":
    pdf_path = '/Users/domtrotta/Documents/Programming/PDF_to_CSV_Project/sample.pdf'  # Ensure this path is correct
    csv_path = '/Users/domtrotta/Documents/Programming/PDF_to_CSV_Project/output_file.csv'  # Update this path if needed
    main(pdf_path, csv_path)
