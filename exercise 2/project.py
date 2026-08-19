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



def fetch_text(format_url):
    response = requests.get(format_url)

    if response.status_code != 200:
        print(f"error code {response.status_code}")
        return

    return response.text



def clean_and_tokenize(text):
    text = text.lower()


    for char in ". , ; : ! ?":
        text = text.replace(char, " ")

    words = text.split()

    return words




def print_books_detailed_info(book):
    print(book["title"])

    for author in book["authors"]:
        print(author["name"], author["birth_year"], author["death_year"])

    print(book["subjects"])
    print(book["bookshelves"])
    print(book["languages"])
    print("Downloads:", book["download_count"])

    if book["copyright"] == True:
        print("Copyright: true")
        print("true -> The book is protected by copyright")

    elif book["copyright"] == False:
        print("Copyright: false")
        print("false -> The book is not protected by copyright")

    elif book["copyright"] == None:
        print("Copyright: none")
        print("null -> The copyright status is unknown or not provided")

    formats = book["formats"]
    format_url = None

    for num, format in enumerate(formats, start=1):
        print(num, format)

    choice = int(input("choose a format: "))

    for num, format in enumerate(formats, start=1):
        if num == choice:
            format_url = formats[format]
            break


    if format_url is None:
        print("Invalid format choice.")
        return

    
    text = fetch_text(format_url)

    words = clean_and_tokenize(text)

    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1

        else: 
            word_counts[word] = 1


    word_list = list(word_counts.items())


    for i in range(len(word_list)):
        for j in range(i + 1, len(word_list)):
            if word_list[i][1] < word_list[j][1]:
                word_list[i], word_list[j] = word_list[j], word_list[i]


    for word, count in word_list[:20]:
        print(word, count)


def main():
    params = {}
    personal_library = {}
    book = None
    book_id = None
    params["sort"] = "popular"
    base = "https://gutendex.com/books"
    data = fetch_books_page("https://gutendex.com/books")

    books = data["results"]
    next_url = data["next"]
    previous_url = data["previous"]



    while True:
        print("1. Show next page")
        print("2. Show previous page")
        print("3. Search by keyword")
        print("4. Filter by language")
        print("5. Filter by topic")
        print("6. Sort by ID")
        print("7. Reset filters")
        print("8. Show details of book by ID")
        print("9. Add current book to personal library")
        print("10. List personal library")
        print("0. Quit")

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

            params["sort"] = sort

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
            book_id = int(input("enter a book id: "))

            if book_id in personal_library:
                book = personal_library[book_id]

            else:
                url = "https://gutendex.com/books/" + str(book_id)
                data = fetch_books_page(url)
                book = data


            print_books_detailed_info(book)

        elif choice == 9:
            personal_library[book_id] = book
            print("current book has been saved")

        elif choice == 10:

            for book_id, book in personal_library.items():
                print(f"[ID]: {book_id} Title: {book['title']} ", end="")
            
                if book["authors"]:
                    print(f"Author: {book['authors'][0]['name']} ", end="")
            
                if book["languages"]:
                    print(f"Language: {book['languages'][0]}", end="")
            
                print()

        elif choice == 0:
            print("Quiting..")
            break


        


if __name__ == "__main__":
    main()