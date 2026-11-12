# English Quiz

Interactive English vocabulary trainer written in Python.

The application allows users to test their vocabulary knowledge using multiple-choice questions. Words can be filtered by level, topic, and part of speech.

## Features

- Multiple-choice questions
- English → Russian translation practice
- Vocabulary filtering by CEFR level (A1-C2)
- Vocabulary filtering by topic
- Vocabulary filtering by part of speech
- Score calculation
- Progress tracking
- Quiz statistics storage in JSON format

## Vocabulary Topics

- Daily Routines
- Animals
- Food and Drinks
- Travel
- Transport
- Hobbies
- Work
- Furniture
- Kitchenware
- Entertainment
- Appearance
- Personality Traits
- Feelings and Emotions

## Supported Levels

- A1
- A2
- B1
- B2
- C1
- C2

## Supported Parts of Speech

- Nouns
- Verbs
- Adjectives
- Pronouns

## Project Structure

```text
english-quiz/
│
├── quiz.py
│
├── data/
│   └── words.json
│
├── results/
│   └── scores.json
│
├── README.md
│
└── .gitignore
```

## Data Format

Example entry from `words.json`:

```json
{
    "word": "cat",
    "translation": "кот",
    "level": "A1",
    "topic": "animals",
    "part_of_speech": "noun"
}
```

## Run

Make sure Python 3 is installed.

```bash
python quiz.py
```

or

```bash
py quiz.py
```

## Example

```text
=== English Quiz ===

Choose level: A1
Choose topic: animals

Question 1

Translate:
cat

1. кот
2. собака
3. лошадь
4. лев

Your answer: 1

Correct!
```

## Statistics

The application stores quiz statistics in `results/scores.json`.

Example:

```json
{
    "games_played": 12,
    "best_score": 95,
    "average_score": 82
}
```

## Technologies

- Python 3
- JSON
- Random module

## Future Improvements

- Russian → English mode
- Flashcard mode
- Difficulty selection
- Learning progress tracking
- Graphical user interface (Tkinter)
- Web version (Flask/FastAPI)

## Author

GitHub: icherzahlung
