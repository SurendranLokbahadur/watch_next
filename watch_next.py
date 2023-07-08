
import spacy                                       # importy NLP library

nlp = spacy.load('en_core_web_md')                 # loading NLP library in order to use

def movie_suggestion(recommended_movie_to_user ): # defining-function that takes the movie-description as a parameter
    
    with open('movies.txt', 'r') as file:         # It opens the movies-list that is inside the text    
        available_movies = [line.strip() for line in file.readlines()] # Reads each line/sentence from the list and removes-space
        input_doc = nlp(recommended_movie_to_user ) # using NLP to analyse the meaning of the user's watched movie-description
        similarities = []                           # creating an empty list to store the similarites between sentences
    
    for movie in available_movies:                  # using condition to repeat the each-sentence inside the list/available_movies
        movie_doc = nlp(movie)                      # using NLP to analyse the meaning of the available-movies inside the list
        comparing_similarity = input_doc.similarity(movie_doc) # analysing the similarity between watched-move & available-movies
        similarities.append(comparing_similarity)              # adding the number of similarities to find the highest-possibility
    
    likelihood_similarity = similarities.index(max(similarities)) # finds the highest-similarity from the movies-list
    return available_movies[likelihood_similarity]  # it returns the movie-description in order to recommend it to the user

# storing the watched movie-description inside the variable
description_of_Watched_Movie = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
recommended_movie_to_user = movie_suggestion(description_of_Watched_Movie) # calling the function

print("RECOMMENDED MOVIE FOR THE USER IS",recommended_movie_to_user) # printing movie-description in order to recommend it to the user
print()