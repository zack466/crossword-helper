# ~Crossword~ Word Search Helper

## Usage

Interactive:

```
python crossword.py --interactive <filename>
```

With Piping:

```
cat <wordlist> | python crossword.py <filename>
```

Try the above commands with `state_capitals.txt` and `words.txt`!

## FAQ

- What does "ldiag N from left" or "rdiag N from right" mean?
  - Starting at the top left or top right corner, count N to the right/left, turning past the corner of the crossword if necessary. The word was found on the diagonal you end at.
  - "Left diagonals" go from the bottom left to the top right, while "right diagonals" go from the top left to the bottom right.
- Why is this called "crossword helper" when in reality it helps solve word searches?
  - Because I'm dumb
