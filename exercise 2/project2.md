## Project: Python Library System with the Gutendex API

### Overview

In this project, you build a small command‑line “library system” in Python that talks to an online book database called Gutendex and processes text from book links. The project is split into parts; each part extends the previous code so that you gradually add features and practise using APIs and data structures.

***

## Pre‑task: Explore the Gutendex API in your browser

Before writing any Python code, get a feel for the API by trying some URLs in your browser.

1. Open a browser and visit these addresses:

   - Basic list of books (first page, most popular):
     - `https://gutendex.com/books`  
       This returns JSON with fields like `count`, `next`, `previous`, and `results` (an array of books). [gutendex](https://gutendex.com/)

   - Search for books by author/title keywords:
     - `https://gutendex.com/books?search=dickens%20great`  
       This includes *Great Expectations* by Charles Dickens. [gutendex](https://gutendex.com/)

   - Filter by language:
     - `https://gutendex.com/books?languages=en`
     - `https://gutendex.com/books?languages=fr,fi`  
       These give books in English, or in French/Finnish, respectively. [gutendex](https://gutendex.com/)

   - Filter by topic (bookshelves/subjects):
     - `https://gutendex.com/books?topic=children`  
       This gives books related to “Children’s Literature”, “Sick children — Fiction”, etc. [gutendex](https://gutendex.com/)

   - Individual book by ID:
     - `https://gutendex.com/books/11`  
       (Try replacing `11` with other numbers.)

2. Look at the JSON structure:
   - Notice top‑level keys like `count`, `next`, `previous`, and `results`.
   - Inside `results`, each book has keys such as:
     - `id`, `title`, `authors`, `languages`, `bookshelves`, `subjects`, `download_count`, `formats`, etc. [gutendex](https://gutendex.com/)
   - Notice that `authors` is a list of objects with `name`, `birth_year`, and `death_year`. [gutendex](https://gutendex.com/)

3. Write down (on paper or in a text file)  answers to these questions:
   - What fields exist for a single book?
   - How do you know where the “next page” of results is?
   - How would you get only English books that mention “children” in their topics?

4. Watch the following video to understand HTTP basics:
   - https://www.youtube.com/watch?v=whH3WI0Gg6E

You will use this understanding in the next parts.

***

## Notes and hints: REST APIs, HTTP, and calling them from Python

Read these notes before you start coding. Refer back to them during the project.

### What is a REST API?

- An API (Application Programming Interface) is a way for one program (the client) to talk to another program or service (the server) to request data or perform actions. [ibm](https://www.ibm.com/think/topics/rest-apis)
- A REST API is a type of web API that follows certain design principles (called “Representational State Transfer”). It typically uses HTTP methods like `GET`, `POST`, `PUT`, and `DELETE` to work with resources (things like “books”, “users”, etc.). [techtarget](https://www.techtarget.com/searchapparchitecture/definition/RESTful-API)
- In this project:
  - The client is your Python code.
  - The server is Gutendex.
  - The resources are books and lists of books, exposed via URLs like `/books` and `/books/<id>`. [gutendex](https://gutendex.com/)

You mainly use HTTP `GET` requests to read data (you are not modifying anything on the server).

### What does an API call entail?

When you “call” a REST API over HTTP:

1. You choose an endpoint URL (for example, `https://gutendex.com/books?languages=en`). [gutendex](https://gutendex.com/)
2. You choose an HTTP method (here: `GET`).
3. You send the request from your program to that URL.
4. The server responds with data, often in JSON format, plus an HTTP status code (such as `200` meaning “OK”). [redhat](https://www.redhat.com/en/topics/api/what-is-a-rest-api)
5. Your program reads the response and turns the JSON text into data structures (lists, dictionaries) that you can work with.

### Calling the API from Python

You can use the `requests` library (or standard `urllib`) to make HTTP calls from Python.

Basic pattern with `requests`:

```python
import requests

url = "https://gutendex.com/books"
response = requests.get(url)

# Check the status code
print(response.status_code)  # 200 means OK

# Parse JSON into Python data structures (dicts/lists)
data = response.json()
```

This pattern is typical: `requests.get(url)` returns a response object, and `.json()` converts JSON text into a Python dictionary (with nested lists and dictionaries). [twpower.github](https://twpower.github.io/124-python-requests-usage)

Think of the JSON you saw in the browser as something that becomes nested `dict` and `list` objects in Python.

***

## Project structure and parts

Follow the parts in order. Each part builds on the previous one. Keep your code organised in functions so that later parts can reuse them.

### Part 1 – Basic book listing

Goal: Make the first API call in Python and display a simple list of books.

Tasks:

1. Write a function `fetch_books_page(url)` that:
   - Takes a URL (string) like `"https://gutendex.com/books"`.
   - Sends an HTTP `GET` request.
   - Returns the parsed JSON data (a Python dictionary from `response.json()`).

2. In your main program:
   - Call `fetch_books_page("https://gutendex.com/books")`.
   - Extract the `results` list from the returned dictionary.
   - For each book in `results`, print:
     - `id`
     - `title`
     - First author’s name (if available)
     - First language code (if available)

3. Design your output so that it is readable, for example:

   ```
   [ID] 11  Title: Alice’s Adventures in Wonderland  Author: Carroll, Lewis  Language: en
   ```

Hints:

- Treat each book as a dictionary; use `book["title"]`, `book["id"]`, etc. [gutendex](https://gutendex.com/)
- `book["authors"]` is a list; check that it is non‑empty before accessing index 0. [gutendex](https://gutendex.com/)
- Remember your C experience: you can think of `results` as an array and each book as a struct with fields.

***

### Part 2 – Pagination and keyword search

Goal: Navigate pages of results and search by keyword.

Tasks:

1. Extend `fetch_books_page(url)` so that it can be reused for any Gutendex URL (including `next`/`previous` URLs).

2. Add a simple command‑line menu in your main program:

   - Option 1: “Show next page”
   - Option 2: “Show previous page”
   - Option 3: “Search by keyword”
   - Option 4: “Quit”

3. Start with the URL `"https://gutendex.com/books"` and store:
   - The current page’s JSON data.
   - The `next` and `previous` URLs from the JSON (`data["next"]` and `data["previous"]`). [gutendex](https://gutendex.com/)

4. When the user chooses:
   - “Show next page”:
     - If `next` is not `None`, call `fetch_books_page(next)` and update current page.
   - “Show previous page”:
     - If `previous` is not `None`, call `fetch_books_page(previous)` and update current page.
   - “Search by keyword”:
     - Ask the user for a search string (e.g. `dickens great`).
     - Build a URL like `https://gutendex.com/books?search=<encoded_key_words>`.
     - Fetch and display the results using the same listing format as Part 1. [gutendex](https://gutendex.com/)

Hints:

- The search parameter `search` looks at author names and titles. [gutendex](https://gutendex.com/)
- You can start by simply replacing spaces with `%20` yourself or use `urllib.parse` to encode the query string.
- Keep the code modular: one function for fetching, one for printing book lists, and the main loop for menu logic.

***

### Part 3 – Filtering and sorting

Goal: Add filters for language, topic, and sorting order using query parameters.

Tasks:

1. Add menu options to allow the user to set filters:
   - “Filter by language”
   - “Filter by topic”
   - “Sort by ID (ascending/descending)”
   - “Reset filters”

2. Build URLs using these Gutendex parameters: [gutendex](https://gutendex.com/)

   - `languages=en` or `languages=en,fr`
   - `topic=children`
   - `sort=ascending`, `sort=descending`, or `sort=popular` (popular is default). [gutendex](https://gutendex.com/)

3. Design a function `build_url(base, params)` that:
   - Takes a base URL like `"https://gutendex.com/books"`.
   - Takes a dictionary `params` mapping parameter names (`"languages"`, `"topic"`, `"sort"`) to string values.
   - Returns a full URL with query string.

4. Use `build_url` whenever the user changes filters, so your API calls always reflect the current filter state.

Hints:

- Think of the `params` dictionary as a map from parameter name to parameter value, similar to a map of key‑value pairs in C.
- You can reuse Part 1’s listing function to display filtered results.
- If multiple parameters are active (e.g. language and topic), all should be included in the query string.

***

### Part 4 – Detailed book view and formats

Goal: View full metadata for a single book and see available text formats.

Tasks:

1. Add a menu option “Show details of book by ID”.

2. When chosen:
   - Ask the user for a book ID (integer).
   - Call the API endpoint `https://gutendex.com/books/<id>` using `fetch_books_page` (or a separate `fetch_book_by_id` function). [gutendex](https://gutendex.com/)
   - Display:
     - `title`
     - All authors´ names and years
     - `subjects`
     - `bookshelves`
     - `languages`
     - `download_count`
     - `copyright` (and explain briefly what `true`/`false`/`null` mean). [gutendex](https://gutendex.com/)

3. For the `formats` field:
   - It is a dictionary mapping MIME type strings to URLs, e.g. `"text/plain; charset=utf-8": "https://..."`. [gutendex](https://gutendex.com/)
   - Print a numbered list of all formats.
   - Let the user select one format by number.
   - Store the chosen format’s URL for use in the next part.

Hints:

- Treat `formats` as a dictionary; iterate over `formats.items()` to get `(mime_type, url)` pairs. [gutendex](https://gutendex.com/)
- Use your C knowledge: think of this as a map from a string key to a string value.
- Add simple error handling: if an ID does not exist, print an error message.

***

### Part 5 – Word‑frequency analyzer from a text link

Goal: Download text from a chosen link and count how often each word appears.

Tasks:

1. Take the selected format URL from Part 4 (or let the user paste any text URL) and download the content:
   - Use `requests.get(format_url)` and `response.text` to get the raw text.

2. Implement a function `clean_and_tokenize(text)` that:
   - Converts all characters to lowercase.
   - Removes punctuation (at least basic characters like `. , ; : ! ?`).
   - Splits the string into words based on spaces and possibly other delimiters.
   - Returns a list of words.

3. Implement a word‑frequency counter using plain Python data structures:
   - Create an empty dictionary `word_counts = {}`.
   - Loop through the list of words:
     - If `word` is already in `word_counts`, increment the count.
     - Otherwise, add it with count 1.

4. After counting:
   - Convert the dictionary into a list of `(word, count)` pairs.
   - Sort the list by count in descending order.
   - Print the top N words (for example, top 20), like:

     ```
     the  520
     and  412
     alice  180
     ```

Hints:

- Do not use `collections.Counter` or other helpers; implement the counting logic yourself to practise dictionaries.
- This is similar to counting frequencies in an array in C, but here you can use a dictionary instead of a fixed‑size array.
- Consider ignoring very short words (like one‑letter words) or provide an option for this.

***

### Part 6 – Local “personal library” and caching

Goal: Save books locally and avoid repeated API calls for the same ones.

Tasks:

1. Add a menu option “Add current book to personal library”.
   - When the user is viewing detailed information for a book (Part 4), allow them to save it.

2. Design an in‑memory data structure for the personal library:
   - For example, a dictionary mapping book ID to a book dictionary:
     - `personal_library = { book_id: book_data_dict }`.

3. Add a menu option “List personal library”:
   - Iterate over `personal_library` and print summary lines for each saved book (ID, title, first author, language).

4. Add simple caching:
   - For fetching book details by ID, first check if the book is already in `personal_library`.
   - If it is, use the cached data instead of calling the API again.
   - If not, call the API and then optionally add it to `personal_library`.

Hints:

- This is like keeping a local array of structs in C, but with a dictionary keyed by ID for faster lookup.
- You can later extend this to saving/loading the library from a JSON file using the `json` module, but for now keeping it in memory is enough.

***

### General coding guidelines

- Use functions to break down the problem:
  - Fetching data (`fetch_books_page`, `fetch_book_by_id`).
  - Printing lists of books.
  - Building URLs with parameters.
  - Cleaning and tokenizing text.
  - Counting word frequencies.
- Keep variables and function names meaningful (e.g. `current_page_data`, `filters`, `personal_library`).
- Use your C experience:
  - Think about time complexity when you design loops and data structures.
  - Avoid unnecessary repeated scanning of the same data.
- Document your code with short comments where the logic might be non‑obvious.

***

This completes the outline of the assignment. Work through the parts in order and keep all code in a single project directory so that later parts can reuse earlier code.