import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import os.path as path


class Clean:
  
    def opening(path):
        """This function opens a csv file and creates a dataframe with the data it contains.

        Args:
            path (string): path where the csv file is located

        Returns:
            dataframe: dataframe with the data contained in the csv file
        """
        df = pd.read_csv(path)
        print('Successful dataframe opening')
        return df
        

    def delete_duplicates_nulls(df):
        """ This function removes duplicate values. It also removes columns with more than 70% null values ​​depending on whether the user wants to remove them or not.

        Args:
            df (dataframe): dataframe from which those columns with a percentage of nulls greater than 70% and duplicate values ​​will be removed.
        """
        
        if df.duplicated().sum() != 0:
            df.drop_duplicates(inplace = True)
            

        null = pd.DataFrame(((df.isnull().sum()) / len(df)) * 100)
        high_percentage_nulls = null[null[0] > 70]
        
        if len(high_percentage_nulls) > 0:
            
            print(f"Columns '{high_percentage_nulls.index[0]}' and '{high_percentage_nulls.index[1]}' have more than 70% null values. Do you want to delete them? (y/n):")
            user_response = input().lower()
            while user_response != 'y' and user_response != 'n':
                print("Invalid term. Please enter 'y' or 'n'.")
                user_response = input().lower()
            
            if user_response.lower() == 'y': 
                delete_columns = high_percentage_nulls[high_percentage_nulls > 70].index
                df.drop(delete_columns, axis = 1, inplace = True)
                print(f"Columns '{high_percentage_nulls.index[0]}' and '{high_percentage_nulls.index[1]}' have been deleted ")
                
            else:
                print('No columns have been delete')
                
            
            print(f'{df.duplicated().sum()} rows with duplicate values ​​have been removed')  
            
        else:
            print('There are no columns with a high percentage of null values')
         
            
    
    def change_to_integer(df, *args):
        """This function changes the data type of the desired columns to integer.

        Args:
            df (dataframe): dataframe in which the columns that need to be modified are located.

        Returns:
            dataframe: dataframe with modified data type
        """
        df_without_nulls = df.replace([np.inf, -np.inf], np.nan).dropna()
        
        columns = list(args)
        for col in columns:
            try:
                df_without_nulls[col] = df_without_nulls[col].astype('int')
            except:
                df_without_nulls[col] = df_without_nulls[col].str.replace(',', '').astype('int')
        
            print(f'The {col} column is now of type {df_without_nulls[col].dtypes}')
        
        return df_without_nulls   
    

    
    def unify_names_classification(rating):
        """ This function unifies the different movie classifications into fewer categories.

        Args:
            rating (string): text that we are going to modify

        Returns:
            string: modified text
        """
        
        if rating == 'R' or rating == 'TV-MA':
            return '17 years or more'
            
        elif rating == 'PG' or rating == 'TV-PG':
            return 'parental guide'
            
        elif rating == 'G' or rating == 'TV-G' or rating == 'Passed' or rating == 'Approved' or rating == 'AL' or rating == 'TV-Y': 
            return 'All public'
            
        elif rating == 'Not Rated' or rating == 'Unrated':
            return 'unclassified'
            
        elif rating == 'PG-13':
            return '13 years or more'
        
        elif rating == '6':
            return '6 years or more'
            
        elif rating == 'TV-14':
            return '14 years or more'
            
        elif rating == '7+':
            return '7 years or more'
        
            
             
    def separate_genre(df, pattern, column):
        """This function separates a list of items by commas and creates a new row for each of the items in the list.

        Args:
            df (dataframe): dataframe that we will modify
            pattern (string): pattern by which we will separate the list
            column (string): name of the column that we will modify

        Returns:
                dataframe: modified data frame
            """
        
        df[column] = df[column].str.split(pattern, n = -1) 
        df = df.explode(column)
        
        if df[column].isnull().sum() != 0: 
            df.dropna(subset= [column], inplace = True) 
            
        else:
            print('New rows have been created in the dataframe')
            
        return df
    


    def save_dataframe(df, path):
        """ This function saves the dataframe to a csv file in the path you specify.

        Args:
            df (dataframe): dataframe that is saved
            path (string): path where the clean dataframe is saved
        """
        
        check_file = os.path.isfile(path)
        
        if check_file == True: 
            print('That name already exists')
            
        else: 
            df.to_csv(path)
            print('Data has been saved successfully')