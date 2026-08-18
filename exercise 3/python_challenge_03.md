# Python Challenge 03

**Dated: 19th of August, 2026**

Read all the instructions below carefully.

## Submission rules

- Where a part's solution is short (a few lines), you may keep sub-parts in the same file. Mark each sub-part with a comment before its code, e.g. `# solution to 2a`.
- Where a part involves running experiments, save your timing results as you go (a `.csv`, a text file, a printed table — your choice) and commit them. **Do not delete or "clean up" results that look surprising.** If a result looks wrong or weird, investigate it and write down what you found, even if you don't fully resolve it.
- Make **multiple commits** that show your progress (e.g., after the generator works, after each exercise, after each experiment) — not one final commit at the end.
- Use of ChatGPT, Gemini, or any AI code generation tool is **not allowed** for this exercise.
- Documentation, official Python docs, search engines, and Stack Overflow **are allowed** — for learning what a function does, understanding an error message, or looking up syntax. There is a difference between researching *how Python works* and looking up *the solution to this exercise*. Stay on the right side of that line.
- Do not submit any code you do not understand or could not explain out loud. Debug problems yourself first; ask for help only after you've tried.
- Push your complete solution, your generator, and your experiment results/notes to the repo.

---

## The situation

You're handed two datasets from a small shop's records: a list of **customers** and a list of **orders**. Every order was placed by some customer, and you need to be able to quickly answer questions that require connecting the two — like "who bought this order?" or "how much has this customer spent in total?"

The datasets start small enough that any code you write will look like it works fine. Later, they will not stay small. Your job across this exercise is to notice when your code stops being "fine" and figure out what to do about it.

---

## Part 0 — Setting up your data

### The shape of the data

Your customers look like this:

```python
{"id": 1, "name": "Aiko Tanaka", "city": "Munich", "signup_year": 2021}
```

Your orders look like this:

```python
{"order_id": 5001, "customer_id": 1, "item": "Keyboard", "amount": 49.99}
```

Notice the join key is called `id` on one side and `customer_id` on the other — don't assume they're always named the same thing.

### 0a — Build the generator

Write a function `make_customers(n)` that returns a list of `n` customer dictionaries, with sequential ids starting at `1`, random names (you can hardcode a small list of first/last names and combine them randomly, or make up your own approach), a random city from a short list of your choosing, and a random `signup_year` (e.g. between 2015 and 2025).

Write a function `make_orders(m, num_customers)` that returns a list of `m` order dictionaries, with sequential `order_id`s, a random `item` from a fixed list (e.g. `["Keyboard", "Mouse", "Monitor", "Laptop", "Cable", "Webcam"]`), and a random `amount` (e.g. a float between 5 and 500).

For the `customer_id` field: pick a random existing customer id (between `1` and `num_customers`) for **all but exactly 5** of the orders. For those 5 orders, assign a `customer_id` that cannot possibly exist — for example `num_customers + 1000`, `num_customers + 1001`, and so on. These 5 are your **orphan orders**: they simulate messy real-world data, like a customer who was deleted after placing an order. This is intentional, not a bug in your generator — every dataset you generate will have exactly 5 unmatched orders, no matter how large it is.

Do not worry about making your data reproducible (no fixed seed needed). Regenerating your data each run is fine, and it will actually help you later — it means you can't accidentally rely on memorized quirks of one specific dataset.

**Hint:** the `random` module has functions for picking a random integer in a range, and a separate one for picking a random item out of a list.

### 0b — Sanity-check your generator

Generate a small dataset (say, 20 customers and 100 orders) and confirm by hand or with a small script that exactly 5 orders are orphans. Write a one-line check you could reuse on any dataset size to confirm this stays true — you'll want it again later.

---

## Part 1 — Getting to know your data

Before joining anything, get comfortable with each list on its own. Generate a small dataset (e.g. 15 customers, 60 orders) and answer the following. Each of these should be a small, mostly one-line piece of code — don't overthink it.

- 1a. Get a list of just the customer names, in the order they appear.
- 1b. Find the customer with the earliest `signup_year`. What about the most recent?
- 1c. Get the last 5 customers in the list without counting how many customers there are.
- 1d. How many orders were placed for a `"Laptop"`?
- 1e. What is the total amount across all orders?
- 1f. Which single order has the highest `amount`? Return the whole record, not just the amount.
- 1g. Get a list of all distinct cities that appear among your customers (no duplicates).
- 1h. Find the customer whose `id` is `7`. What should your code do if no such customer exists in this particular dataset?

**Hints, if you want them:**
- For 1a: a list comprehension is a natural fit here.
- For 1b/1f: Python has a built-in for finding the maximum/minimum of a sequence, and it accepts a way of telling it *what to compare by*.
- For 1c: lists support slicing with negative positions.
- For 1g: think about a built-in data structure that automatically de-duplicates.
- For 1h: consider what happens with a comprehension or generator combined with a built-in that stops at the first match.

Keep this code — you'll be reusing pieces of it soon.

---

## Part 2 — The obvious way to connect the two lists

Now the real task: for each order, find the customer who placed it.

### 2a — Write the naive join

Write a function `find_customer_for_order(order, customers)` that takes a single order and the full customer list, and returns the matching customer dictionary — searching through `customers` one at a time until it finds a match.

Some orders won't have a matching customer (remember the orphans). Decide what your function should do in that case — just make sure it doesn't crash, and pick a return value that makes sense to you (and that you can explain).

### 2b — Join everything

Write a function `join_all(orders, customers)` that uses `find_customer_for_order` to build a combined result for *every* order — however you find natural to represent one matched pair (a tuple, a new merged dictionary, whatever makes sense to you).

Test it on your small dataset from Part 1. Confirm that exactly 5 orders end up unmatched.

### 2c — Time it

Before anything else, get used to timing code. Python's `time` module has a function called `perf_counter()` that gives you a precise clock reading; call it before and after your join runs, and look at the difference.

Run `join_all` on your small dataset and record how long it takes.

Then generate a noticeably bigger dataset — say 2,000 customers and 10,000 orders — and time it again.

**Questions to think about (write down your answers, even briefly):**
- Was one timing measurement enough, or did you notice the number change if you ran it again on the same data? Why might that be?
- Before running the bigger dataset, guess: roughly how much slower do you expect it to be? Were you right?

---

## Part 3 — Turning up the size

This is where the shape of the problem starts to matter.

### 3a — Scale it up, deliberately

Generate several datasets of increasing size — for example, keep the ratio of orders to customers roughly fixed (say, 5 orders per customer) and grow both, at sizes like 100, 1,000, 10,000, and 50,000 customers. Run `join_all` on each, timing every run, and record your results (a simple table: dataset size → time taken).

Run each size more than once. Note whether the times are stable or jump around.

### 3b — Look at your numbers

Look at your table. As the dataset grows by roughly 10×, what happens to the time? Does it grow by about the same factor, more, or less? Try to describe what you see in your own words — no need for any formal terminology.

At this point, you don't need to fix anything yet. Just make sure you've actually *felt* the slowdown by watching it happen, not by being told about it.

---

## Part 4 — Trying a different approach: sort, then search

One idea: if the customers were sorted by `id`, you wouldn't have to scan through all of them to find a match — you could narrow down where to look. This requires two new pieces: a way to sort, and a smarter search that takes advantage of that sorting.

### 4a — Bubble sort, by hand

Implement `bubble_sort(records, key)` that sorts a list of dictionaries by a given field (`key` is the field name to sort by), using the bubble sort algorithm — repeatedly stepping through the list and swapping adjacent elements that are out of order. Test it on a small customer list sorted by `id`, and confirm it actually produces a correctly sorted list.

### 4b — Bubble sort vs. `sorted()`

Time your `bubble_sort` against Python's built-in `sorted()` (with an appropriate `key=` argument) on the same customer lists, at increasing sizes.

Then try this with three different kinds of input at the same size:
- randomly generated customers (as usual),
- a list that's already sorted by `id`,
- a list that's sorted in reverse.

**Questions to think about:**
- Does `bubble_sort` behave the same way on all three kinds of input, or does something change?
- Does `sorted()` care which kind of input it gets? Can you tell from the timings?
- Before running each case, try predicting what will happen. How often were you right?

### 4c — Binary search

Implement `binary_search(sorted_records, key, target_value)` that searches a **sorted** list of records for the one whose `key` field equals `target_value`, using binary search — repeatedly checking the middle of the remaining range and narrowing down to one half.

Test it against a few known values (including a value you know isn't there) on a small sorted customer list, comparing against what a plain linear scan would give you.

### 4d — Join, take two

Write `join_all_sorted(orders, customers)` that sorts `customers` by `id` (using `sorted()`, not your bubble sort — you already know why) and then uses `binary_search` to find the match for every order.

Run this on the same increasing dataset sizes as Part 3a, and time it two different ways:

- **Total time**, including the sort itself, every time.
- **Search-only time**, where you sort once and then only time the repeated lookups (imagine the customer list arrives already sorted, or you only need to sort it once and then handle many orders afterward).

Add both to your results table alongside the Part 3 numbers.

**Questions to think about:**
- Does including the sort time change your conclusion about which approach is faster?
- At what dataset size (roughly) does the sorted+binary-search approach start winning, if it does?
- Is there a size where it *doesn't* win? Why might that be?

---

## Part 5 — Trying a different data structure

Sorting and searching is one idea. Here's another: what if you didn't need to search at all?

### 5a — Index the customers

Build a dictionary that maps `customer_id → customer record`, built once from your customer list.

### 5b — Join, take three

Write `join_all_dict(orders, customers)` that builds this dictionary once and then looks up each order's customer directly through it.

You'll hit the orphan orders again here — decide how to handle a missing key. (There's more than one idiomatic way to do this in Python; if you're not sure, look into what a dictionary's `.get()` method does, or how a `try`/`except` around a dictionary lookup behaves.)

### 5c — Time all three, together

Using the same dataset sizes as before, time `join_all`, `join_all_sorted` (both variants from 4d), and `join_all_dict`, and put every result in one combined table.

**Questions to think about:**
- Which approach wins at small sizes? Does the same one win at large sizes?
- Does building the dictionary itself cost anything noticeable? Does that cost matter at the sizes you tested?
- If you had to process a million orders against the same customer list, which approach would you pick, and why — based on your data, not a guess?

---

## Part 6 — Writing it up

In a short `NOTES.md` (or similar) in your `exercise3` folder, answer the following in your own words. A few sentences per question is enough — this isn't an essay.

- Summarize what you observed across Parts 3–5. Which approach was fastest, and did that change as the data grew?
- Was there anything that surprised you? (If yes — did you investigate it? What did you find?)
- Did any of your predictions (Parts 2c, 4b, 4d) turn out wrong? What made you revise your thinking?
- Why do you think repeated timing measurements of the "same" code sometimes give different numbers?
- If someone asked you "which is faster, searching a list or looking something up in a dictionary?" — how would you answer now, based on what you measured, without needing to explain *why* in theoretical terms?

---

## What to submit

- Your generator code (`0a`, `0b`).
- Your Part 1 answers.
- All three join implementations (`join_all`, `join_all_sorted`, `join_all_dict`) and their supporting functions (`find_customer_for_order`, `bubble_sort`, `binary_search`).
- Your timing results — as code, printed output, a saved table, or all of the above.
- `NOTES.md` with your Part 6 write-up.
- A commit history showing incremental progress, not a single commit.
