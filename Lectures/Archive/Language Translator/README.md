<img src="./images/language-translator.png" width="700"/>

# Language Translator
> DIFFICULTY: **INTERMEDIATE**

A language translator is a very handy application that helps us to communicate in different languages by translating our language to the desired language. Our objective is to create a Language Translator which would help us translate a word, sentence or even a paragraph to another language. 

We will try to incorporate as many languages as possible. We will be using **tkinter** Module to build our GUI for the project and **googletrans** library to present us with a number of languages that are a part of it. Also, we will use the **textblob** library for processing textual data.

## Modules

- *tkinter* : This is the module to create easy GUI in Python.
- *messagebox* : This is for displaying a message box.
- *textblob* : This is for analysing and processing textual data.
- *googletrans* : This is for importing a number of languages that we will be using during the project to translate from one to another.

## TODO

1. Import Modules
2. Use *tkinter* to create the GUI screen
3. Define translate function to:
    - Get the text from user
    - Use *textblob* to detect the input and output language
    - Translate from language to another with *textblob*
    - If there is some error raise an Exception
4. Use *googletranse* module to get list of languages.
5. Make text boxes and bottons with *tkinter*

## Result

Your language translator should look like the image below:

<img src="./images/result.png" width="400"/>
