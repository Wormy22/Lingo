#!/usr/bin/env python3
import random
import datetime

CORRECT = "green"
WRONG_POSITION = "orange"
NOT_PRESENT = "-"

# TODO - get better word lists
WORD_LISTS = {4: "four_letter_words.txt",
              5: "five_letter_words.txt"}

valid_words = {4: [],
               5: []}


class LingoException(Exception):
    pass


def initialise():
    global valid_words

    for i in valid_words.keys():
        valid_words[i] = load_words_from_file(i)


def load_words_from_file(num_letters):
    with open(WORD_LISTS[num_letters], "r") as f:
        return f.read().splitlines()


def pick_word(num_letters):
    if num_letters not in valid_words.keys():
        raise LingoException("Can only play with 4 or 5 letter words!")

    # Randomly pick word with seed based on current time
    random.seed(datetime.datetime.now())
    return random.choice(valid_words[num_letters])


def check_guess(guess, answer):
    if len(guess) != len(answer):
        raise LingoException("Guess is not same length as answer.")
    elif guess not in valid_words[len(guess)]:
        raise LingoException(f"{guess} is not a valid word!")

    result = []

    for i, letter in enumerate(guess):
        if letter == answer[i]:
            result.append(CORRECT)
        elif letter in answer:
            result.append(WRONG_POSITION)
        else:
            result.append(NOT_PRESENT)

    return result

initialise()
