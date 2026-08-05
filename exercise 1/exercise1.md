Python Challenge 01:

Dated: 31th of July, 2026
==============================
0. Read all the instruction below carefully.
1. Create a new git repository for Python exercises.
2. Add the solution to this exercises in a folder called exercise1 inside the repo.
3. For simple exercises where the solution of parts is one line, you can write the whole code in a single file. No need to create a different file for a sub-part (like a, b, c).
4. If you write all sub-parts in a single file, write the problem number is comments before the code. For example: solution of 1a.
5. Use of ChatGPT or Google's Gemini (in google search) is not allowed for this exercise.
6. Do not write any code that you do not understand or that you can no explain yourself.
7. Push this file on the repo along with the code.

==========================================================
## Full Exercise Set

### 1. Basics (Types, Casting, Operators, Variables) — single combined exercise

Write a script that does all of the following in one file:

a) Create variables of type int, float, bool, and NoneType, and print their types using type().
b) Cast a float to an int and an int to a float; print results before and after casting.
c) Given two numbers a = 17, b = 5, print the results of a + b, a - b, a * b, a / b, a // b, a % b, a ** b.
d) Predict (in a comment) the type of each result in (c) before running the code, then verify.

*Hint: / always returns a float, even if both operands are ints — this differs from C's integer division.*

### 2. Strings

1. Given a string s = "Introduction to CS", print the first 5 characters, the last 5 characters, and the string reversed.
2. Take a string and print it in all uppercase, all lowercase, and title case.
3. Write code to check whether a given word is a palindrome (reads the same forwards and backwards).
4. Count how many vowels appear in a given sentence.

*Hint: Strings are immutable in Python — you can't change a character in place; slicing (s[::-1]) is the idiomatic way to reverse.*

### 3. Input/Output

1. Ask the user for their name and age using input(), then print a greeting using plain print() with comma-separated arguments.
2. Repeat the same greeting, but format it using the % operator (e.g., "%s is %d years old").
3. Repeat again using .format() method.
4. Repeat again using an f-string.
5. Ask the user for a float (e.g., a price) and print it rounded to 2 decimal places using each of the three formatting styles above.

*Hint: input() always returns a string — you must cast it explicitly (int(), float()) before doing math on it.*

### 4. Branching

1. Write a simple if/else that checks if a number is positive, negative, or zero.
2. Write a program that assigns a letter grade (A/B/C/D/F) based on a numeric score using if/elif/else.
3. Write a leap year checker (divisible by 4, but not by 100 unless also divisible by 400) — this needs nested or combined conditionals.

*Hint: Indentation is not just style in Python — it defines the block structure, unlike curly braces in C.*

### 5. Iteration

1. Use a for loop with range() to print numbers 1 to 20, then modify it to print only even numbers.
2. Use a while loop to repeatedly ask the user for input until they type "quit".
3. Loop over a string character by character and count how many times a specific letter appears.
4. Combine looping and branching: given a number, print the sum of its digits.

*Hint: for loops are best when you know how many times to iterate; while loops are best when the stopping condition depends on runtime behavior.*

### 6. Guess-and-Check Algorithms

1. Implement the square root approximation from Lecture 1 yourself: start with a guess, repeatedly average the guess with x/guess, and stop when the guess squared is within a small tolerance (e.g., 0.0001) of x.
2. Adapt your solution to approximate a cube root instead (guess such that guess ** 3 is close to x) — think about how the "improve guess" step needs to change.

*Hint: Print your guess at every iteration while developing this — it helps you see whether the algorithm is converging or diverging.*

### 7. Binary Search Style Problems

1. Write a number-guessing game: the computer picks a secret number between 1 and 100, and using binary search logic (higher/lower feedback), guess it in as few tries as possible.
2. Given a sorted list of numbers, write a function-free script that finds whether a target number exists in the list using the binary search approach (repeatedly checking the middle element and halving the search range).

*Hint: Always double-check your boundary conditions — off-by-one errors are the most common bug in binary search.*

### 8. Functions — Starter Exercises

1. Write a function add(a, b) that returns the sum of two numbers, then call it and print the result.
2. Write a function is_even(n) that returns True or False depending on whether n is even.
3. Write a function greet(name, greeting="Hello") with a default argument, and call it both with and without specifying greeting.

*Hint: return sends a value back to the caller; print() only displays it on screen — they are not interchangeable, and a function without return implicitly returns None.*

Good call — using `random` makes the simulation more realistic. Here's the updated structure with weather modeling as Part 5, and the final report shifted to Part 6.

## 9. Project: The Lemonade Stand Simulator

**Goal**: Simulate selling lemonade for 7 days, track profit, and find the price that maximizes earnings — using guess-and-check.

### Part 1: Setup

Write a function `day_profit(price, cups_sold, cost_per_cup)` that returns profit for one day: `(price - cost_per_cup) * cups_sold`.

### Part 2: Simulating a Week

- Assume cost_per_cup = 0.30.
- For each of 7 days, ask the user to input how many cups were sold that day.
- Use a loop to collect daily sales, call `day_profit()` each time, and print a running total.

*Hint: initialize total_profit = 0 before the loop and add to it each iteration.*

### Part 3: Reacting to Bad Days (Branching)

Inside the loop, add logic:

- If a day's profit is negative, print "Rough day — consider lowering the price."
- If a day's profit is the best so far, print "New best day!"

*Hint: keep a best_profit variable updated as you loop, compare each day's profit against it.*

### Part 4: Finding the Best Price (Guess-and-Check)

Customers buy fewer cups as the price goes up. Assume this relationship: `cups_sold = max(0, 50 - 40 * price)`.

- Write a loop that tries prices from 0.10 to 2.00 in small steps (e.g., 0.05).
- For each price, calculate expected cups_sold using the formula above, then calculate profit using `day_profit()`.
- Track and print the price that gives the highest profit.

*Hint: this is guess-and-check — you're not solving for the best price with algebra, you're trying many guesses and keeping the best one.*

### Part 5: Modeling Weather with the `random` Module

Instead of asking the user for weather, simulate it randomly each day.

- At the top of your file, add `import random`.
- Use `random.choice(["sunny", "rainy", "cloudy"])` to pick a weather type for each day in your loop.
- On "rainy" days, reduce cups_sold by 50%. On "cloudy" days, reduce by 20%. "Sunny" days are unaffected.
- Print the day's weather along with its profit, so you can see the effect.

**Pointers on the `random` module**:

- `random.choice(list)` picks one random item from a list — perfect for categorical choices like weather.
- `random.randint(a, b)` returns a random integer between a and b (inclusive) — useful if you want to simulate cups_sold randomly instead of typing it in.
- `random.random()` returns a random float between 0 and 1 — handy for probability checks, e.g., "20% chance of rain" via `if random.random() < 0.2`.
- Every run will give different results unless you fix the randomness with `random.seed(some_number)` — useful for debugging so results are reproducible.

*Hint: try running your simulation multiple times without a seed, then again with a seed, to see the difference.*

### Part 6: Final Report (Output Formatting)

Print a summary using an f-string:

- Total profit for the week.
- Best single day, its profit, and that day's weather.
- The optimal price found in Part 4, rounded to 2 decimal places.

*Hint: use f-string formatting like `f"{value:.2f}"` to control decimal places.*