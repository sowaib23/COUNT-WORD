# COUNT WORD

COUNT WORD is a very simple Python desktop app that counts how many words are in a text.

This project is made with **Tkinter**, which is Python's built-in library for creating basic graphical user interfaces.

## What This Project Does

This app lets the user:

- type or paste text into a text box
- click the **Count Words** button
- see the total number of words on the screen

## Who This Project Is For

This project is useful for:

- beginners who are learning Python
- students who want to practice simple GUI programming
- anyone who wants to understand how Tkinter buttons, text boxes, and labels work
- small practice projects for learning functions and regular expressions

Because the project is simple, it is a good starting point for learning how a desktop app works.

## How It Works

The program uses:

- `Tkinter` to create the window, text box, button, and result label
- `re.findall()` to find all words from the text
- a function called `count_words()` to count the words and update the result

When the user clicks the button, the program reads the text from the text box, counts the words, and shows the result.

## How To Use

1. Make sure Python is installed on your computer.
2. Download or clone this project.
3. Open the project folder.
4. Run the Python file:

```bash
python "word counter.py"
```

5. A small window will open.
6. Type or paste your text.
7. Click **Count Words**.
8. The app will show the number of words.

## File

- `word counter.py` - the main Python file that runs the word counter app

## Example

If you type:

```text
I am learning Python
```

The result will be:

```text
Words : 4
```

## Why I Made This

This project was made as a beginner-friendly Python practice project. It helps understand basic GUI design, button actions, text input, and simple word counting logic.
