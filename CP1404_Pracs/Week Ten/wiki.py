"""
Patrick Robinson
12251568
CP1404
Demonstrating the wikipedia API functionality

"""
import wikipedia

search_phrase = str(input("Please enter a search phrase "))  # Getting the search term
while search_phrase != "":
    try:
        print(wikipedia.summary(search_phrase))
        page = wikipedia.page(search_phrase)  # Getting the summary, page title and url
        print(page.title)
        print(page.url)
        search_phrase = str(input("Please enter a search phrase "))
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
