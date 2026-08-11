import requests

def fetch_books_page(url):
    response = requests.get(url)

    if response.status_code != 200:
        print(f"error code {response.status_code}")
        return

    return response.json()


def build_url(base, params):
    list = []

    for i, j in params.items():
        list.append(f"{i}={j}")
    
    string = "&".join(list)
    
    return base + "?" + string


def print_books(books):
    for book in books:
    
            print(f"[ID]: {book['id']} Title: {book['title']} ", end="")
    
            if book["authors"] != []:
                print(f"Author: {book['authors'][0]['name']} ", end="")
    
            if book["languages"] != []:
                print(f"Language: {book['languages'][0]}", end="")
    
            print()
            print()

def main():
    params = {}
    params["sort"] = "popular"
    base = "https://gutendex.com/books"
    data = fetch_books_page("https://gutendex.com/books")

    books = data["results"]
    next_url = data["next"]
    previous_url = data["previous"]

    print_books(books) 

    while True:
        print("1. Show next page")
        print("2. Show previous page")
        print("3. Search by keyword")
        print("4. Filter by language")
        print("5. Filter by topic")
        print("6. Sort by ID")
        print("7. Reset filters")
        print("8. Quit")

        choice = int(input("enter your choice: "))
        if choice == 1:
            if next_url is not None:
                data = fetch_books_page(next_url)
                next_url = data["next"]
                previous_url = data["previous"]
                books = data["results"]
                print_books(books)

        elif choice == 2:
            if previous_url is not None:
                data = fetch_books_page(previous_url)
                next_url = data["next"]
                previous_url = data["previous"]
                books = data["results"]
                print_books(books)

        elif choice == 3:
            key_word = input("enter a key word: ")
            key_word = key_word.replace(" ",  "%20")
            url = "https://gutendex.com/books?search=" + key_word
            data = fetch_books_page(url)
            books = data["results"]
            next_url = data["next"]
            previous_url = data["previous"]
            print_books(books)

        elif choice == 4:
            language = input("which launguage do you want to chosse en or fr: ")

            params["languages"] = language

            url = build_url(base, params)
            data = fetch_books_page(url)
            books = data["results"]
            next_url = data["next"]
            previous_url = data["previous"]
            print_books(books)

        elif choice == 5:
            topic = input("enter the topic you want to search: ")

            params["topic"] = topic

            url = build_url(base, params)
            data = fetch_books_page(url)
            books = data["results"]
            next_url = data["next"]
            previous_url = data["previous"]
            print_books(books)

        elif choice == 6:
            sort = input("enter sort order (ascending/descending/popular): ")

            params["sort"][0] = sort

            url = build_url(base, params)
            data = fetch_books_page(url)
            books = data["results"]
            next_url = data["next"]
            previous_url = data["previous"]
            print_books(books)

        elif choice == 7:
            params = {}
            params["sort"] = "popular"

            print("filters have been reset")

            url = build_url(base, params)
            data = fetch_books_page(url)
            books = data["results"]
            next_url = data["next"]
            previous_url = data["previous"]
            print_books(books)

        elif choice == 8:
            print("Quiting..")
            break


        


if __name__ == "__main__":
    main()