#%%
import subprocess
import sys
from nlplib.log import clear_log, write_log
import nltk
import pandas as pd
import matplotlib.pyplot as plt
from nltk.corpus import gutenberg
from nlplib.nltk import list_nltk_books
from nlplib.config import TEST, TEST_ROWS, BOOK_NAME
from nlplib.log import write_log

def install_requirements():
    subprocess.check_call([
        sys.executable,
        "-m",
        "pip",
        "install",
        "-r",
        "requirements.txt"
    ])
    write_log("Installed the requirements.")

def main():
    #%%
    #1. 
    clear_log()

    if TEST:
        book_list = list_nltk_books()

        write_log(f"The book list from NLTK:", skip_print = True)
        for index, book in enumerate(book_list, start = 1):
            write_log(f"Book {index}: {book}", skip_print = True)

    book = gutenberg.raw(BOOK_NAME)
    write_log(f"Book is chosen as {BOOK_NAME}")

    if TEST:
        book = book[:TEST_ROWS]

    write_log(f"\n----EXTRACT_START----\n{book[:TEST_ROWS]}\n----EXTRACT_END----\n", skip_print = True)
    
#%%
if __name__ == "__main__":
    install_requirements()
    main()
    write_log("The main process ended successfully.")