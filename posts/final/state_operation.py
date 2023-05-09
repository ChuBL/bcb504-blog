import pandas as pd

def state_comparison():
    # List of U.S. states
    us_states = [#'United States', 'District of Columbia', 'New York City',
        'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut',
        'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa',
        'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan',
        'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
        'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma',
        'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee',
        'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'
    ]

    # Read the CSV file
    input_file = 'by_year.csv'
    df = pd.read_csv(input_file)

    # Extract unique state values from the 'State' column
    unique_states_in_csv = df['State'].unique()

    # Compare the unique state values with the U.S. states list
    missing_states = set(us_states) - set(unique_states_in_csv)
    extra_states = set(unique_states_in_csv) - set(us_states)

    print("Missing states:", missing_states)
    print("Extra states:", extra_states)

def state_filter(filename):
    # Read the input CSV file
    #input_file = 'Conditions_Contributing_to_COVID-19_Deaths__by_State_and_Age__Provisional_2020-2023.csv'
    df = pd.read_csv(filename)

    # Filter out rows with 'State' column having the value 'Puerto Rico'
    filtered_df = df[df['State'] != 'Puerto Rico']

    # Write the filtered DataFrame to a new CSV file
    output_file = 'filtered_' + filename
    filtered_df.to_csv(output_file, index=False)

if __name__ == '__main__':
    #state_comparison()
    #state_filter('by_month.csv')
