- Summarize what you observed across Parts 3–5. Which approach was fastest, and did that change as the data grew?
Ans: Across Parts 3–5 i noticed that the approach became more complicated as the data size increased the join_all_dict approach was the fastest and it remained the fastest even when the dataset size changed

- Was there anything that surprised you? (If yes — did you investigate it? What did you find?)
Ans: yes i was very surprised by the Part 4d results the time dropped from around 17 minutes to about 2 seconds after investigating i found that binary search and Python's built-in sorted() made a huge difference

- Did any of your predictions (Parts 2c, 4b, 4d) turn out wrong? What made you revise your thinking
Ans: most of my predictions were wrong only my prediction for join_all_dict was close to the actual result the actual timings were very different from what i expected so the results changed my thinking about which approach would be faster as the data grew

- Why do you think repeated timing measurements of the "same" code sometimes give different numbers?
Ans: when the same code is run multiple times the timing can be slightly different the difference is usually small and can happen because of the CPU load on the computer

- If someone asked you "which is faster, searching a list or looking something up in a dictionary?" — how would you answer now, based on what you measured, without needing to explain *why* in theoretical terms?
Ans: both can be useful depending on the situation but in my tests looking up a customer in a dictionary was faster than searching a list