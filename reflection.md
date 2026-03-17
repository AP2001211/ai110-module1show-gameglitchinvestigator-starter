# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
My first attempt at the game itself made me realise that the hints are backward. Hostory also does not update correctly.
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
    - The hints and guesses were not aligned correctly, for some reason I only got "go lower"
    - New Game button does not reset everything
    - attempts counter baseline wrong
    - check guess is wrong
    - Core game logic was mixed into the UI file instead of the utility module.
    - Hard difficulty was easier than Normal.
    

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
copilot and chatgpt
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
when I pointed out the new_game bug, it agreed and provided a quick fix for this.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
One misleading AI suggestion was to directly assign st.session_state.guess_input = "" after the input widget had already been created in the same run. That sounded correct at first, but it caused a StreamlitAPIException because Streamlit does not allow modifying a widget’s state after instantiation in that way. I verified that it was wrong by running the app and reproducing the exception immediately.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I verified my fixes in two ways: automated tests and manual testing in the Streamlit app. First, I ran the provided starter tests for check_guess, which confirmed that winning, too-high, and too-low guesses behaved correctly. Then I added my own tests for invalid input parsing, difficulty range behavior, and score updates. After all seven tests passed, I reran the app in Streamlit and manually checked that the hints matched the secret number, the score and attempts reset properly, and the New Game button cleared the input box safely.


---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?
I learned that Streamlit reruns the script from top to bottom whenever the user interacts with the page, so values need to be stored carefully in st.session_state if they should persist across interactions. I also learned that widget state cannot always be changed arbitrarily after a widget has already been instantiated in the same run. That mattered for the textbox reset bug, because the fix had to respect how Streamlit manages widget state internally.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to keep is separating logic from UI early, because that made it much easier to write tests and reason about bugs. I also want to keep verifying AI suggestions with real tests and real app behavior instead of assuming the first answer is correct. This project showed me that AI can be a useful debugging partner, but framework-specific issues still require careful manual checking.
