import pandas as pd
import os

# Define the directory where your CSV files are located
directory = "./"

# Initialize an empty DataFrame to store the combined data
combined_data = pd.DataFrame()

# Loop through all CSV files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        # Load the original CSV file
        input_csv_path = filename
        df = pd.read_csv(input_csv_path)

        # Define the custom input you want to add
        custom_input = filename.strip(".csv")

        # Add the custom input as a new column to the DataFrame
        df["company"] = custom_input

        # Save the modified DataFrame to a new CSV file
        output_csv_path = filename
        df.to_csv(output_csv_path, index=False)

        file_path = os.path.join(directory, filename)

        # Read each CSV file into a DataFrame
        data = pd.read_csv(file_path)

        # Concatenate the data to the combined_data DataFrame
        combined_data = pd.concat([combined_data, data], ignore_index=True)

# Now, combined_data contains the data from all CSV files
# You can save it to a new CSV file if needed
combined_data.to_csv("combined_history.csv", index=False)
