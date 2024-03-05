import os
import shutil
import time
import pandas as pd
import glob


def dataframe_creation():

    try:
        df1 = pd.read_csv(r"data_20240224-113829.csv")

        # Read the second CSV file
        df2 = pd.read_csv(r"data_20240224-114329.csv")  
        
        # Concatenate the two dataframes
        #df = pd.concat([df1, df2], ignore_index=True)
        combined_df = pd.concat([df1, df2], ignore_index=True)
                    
        return combined_df
        
    except Exception as e:
        print(f"An error occurred: {e}")

