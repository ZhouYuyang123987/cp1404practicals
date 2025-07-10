"""
CP1404 Assignment 1
Student Name: Zhou Yuyang
Student ID: 14785988
Date Started: 19th June 2025
GitHub Repository:https://github.com/cp1404-students/a1-movies-ZhouYuyang123987
Description: A program to manage a list of movies, allowing users to view, add, mark as watched, and save movies to a CSV file.
"""

import csv

# Named constants
WATCHED = 'w'
UNWATCHED = 'u'
VALID_CATEGORIES = ['Action', 'Comedy', 'Documentary', 'Drama', 'Thriller', 'Other']
MENU = """Menu:
D - Display movies
A - Add new movie
W - Watch a movie
Q - Quit
>>> """
CSV_FILE = 'movies.csv'




CSV_FILE = 'movies.csv'

def main():
    print("Must-See Movies 1.0 - by Mannim Mond")
    movies = load_movies()
    print(f"{len(movies)} movies loaded from {CSV_FILE}")
    
    while True:
        choice = input(MENU).strip().lower()
        if choice == 'q':
            save_movies(movies)
            print(f"{len(movies)} movies saved to {CSV_FILE}")
            print("Have a nice day :)")
            break
        elif choice == 'd':
            display_movies(movies)
        elif choice == 'a':
            add_movie(movies)
        elif choice == 'w':
            watch_movie(movies)
        else:
            print("Invalid menu choice")  


#This function Loads the movies from the given csv file to a list
def load_movies():
    movies = []
    try:
        with open(CSV_FILE, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 4:
                    movies.append([row[0], int(row[1]), row[2], row[3]])
    except FileNotFoundError:
        pass  
    return movies

# This function saves the movies to a CSV file
def save_movies(movies):
    with open(CSV_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        for movie in movies:
            writer.writerow(movie)

#This function shows all the movies in a sorted manner by the year then followed by the titles
def display_movies(movies):
    if not movies:
        print("No movies to display.")
        return
    
    movies.sort(key=lambda x: (x[1], x[0]))
    
    unwatched_count = 0
    max_title_length = max(len(movie[0]) for movie in movies)  
    
    for i, movie in enumerate(movies, 1):
        title, year, category, status = movie
        marker = '*' if status == UNWATCHED else ' '
        print(f"{i}. {marker} {title:<{max_title_length}} - {year} ({category})")
        if status == UNWATCHED:
            unwatched_count += 1
    
    watched_count = len(movies) - unwatched_count
    print(f"{watched_count} movies watched. {unwatched_count} movies still to watch.")


#The below function adds movies to the list after checking for errors from the users
def add_movie(movies):
    title = get_valid_string("Title: ")
    year = get_valid_year()
    category = get_valid_category()
    
    movies.append([title, year, category, UNWATCHED])
    print(f"{title} ({category} from {year}) added to movie list")

#When a user watches a movie, the below function marks it as watched
def watch_movie(movies):
    unwatched_movies = [i for i, movie in enumerate(movies) if movie[3] == UNWATCHED]
    
    if not unwatched_movies:
        print("No more movies to watch!")
        return
    
    movie_number = get_valid_movie_number(len(movies))
    movie_index = movie_number - 1
    movie = movies[movie_index]
    
    if movie[3] == WATCHED:
        print(f"You have already watched {movie[0]}.")
    else:
        movie[3] = WATCHED
        print(f"{movie[0]} ({movie[1]}) watched.")

#ensures the users enters a string
def get_valid_string(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input can not be blank")

# Ensures the year entered by the user is valid
def get_valid_year():
    while True:
        try:
            year = int(input("Year: "))
            if year <= 0:
                print("Number must be > 0")
            else:
                return year
        except ValueError:
            print("Invalid input; enter a valid number")

# Gets a valid category of the movie from the user
def get_valid_category():
    print(f"Categories available: {', '.join(VALID_CATEGORIES)}")
    category = get_valid_string("Category: ").capitalize()
    
    if category not in VALID_CATEGORIES:
        print("Invalid category; using Other")
        return 'Other'
    return category

# The function gets a valid movie number
def get_valid_movie_number(max_number):
    while True:
        try:
            number = int(input("Enter the movie number to mark watched.\n>>> "))
            if number <= 0:
                print("Number must be > 0")
            elif number > max_number:
                print("Invalid movie number.")
            else:
                return number
        except ValueError:
            print("Invalid input; enter a valid number")

if __name__ == '__main__':
    main()
