import src.support as sp

# call to class
cleaner = sp.Clean

# opening method
df_christmas_movies = cleaner.opening('../data_movies/christmas_movies.csv')
print('--------------------')

# delete nulls and duplicates
cleaner.delete_duplicates_nulls(df_christmas_movies)
print('--------------------')

# change data type
df_christmas_movies = cleaner.change_to_integer(df_christmas_movies, 'release_year', 'votes', 'runtime')
print('--------------------')

# unify classification
df_christmas_movies['rating'] = df_christmas_movies['rating'].apply(cleaner.unify_names_classification)
print(f"Now the unique values ​​have been unified into the following: {df_christmas_movies['rating'].unique()}")
print('--------------------')

# create row by gender
df_christmas_movies = cleaner.separate_genre(df_christmas_movies, ', ', 'genre')
df_christmas_movies = cleaner.separate_genre(df_christmas_movies, ', ', 'stars')
print('The data is now ready to be saved and viewed in Power Bi!')
print('--------------------')

# data saving
cleaner.save_dataframe(df_christmas_movies, '../clean_data_movies/clean_christmas_movies.csv')


