import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError

search = input("Enter a page title to search for: ")
while search != "":
    try:
        page = wikipedia.page(search)
        print(f"\n{page.title}\n{page.summary}\n{page.url}\n")
    except DisambiguationError as e:
        print("We need a more specific title. Try one of the following, or a new search:")
        options = e.options
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
    except PageError:
        print(f"Page id '{search}' does not match any pages. Try another id!")
    search = input("Enter a page title to search for: ")
