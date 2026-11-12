import json
import random


def load_words():
    with open("data/words.json", "r", encoding="utf-8") as file:
        return json.load(file)


def load_scores():
    try:
        with open("results/scores.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {
            "games_played": 0,
            "best_score": 0
        }


def save_scores(scores):
    with open("results/scores.json", "w", encoding="utf-8") as file:
        json.dump(scores, file, indent=4)


def get_filtered_words(words, level, topic):
    return [
        word
        for word in words
        if word["level"] == level
        and word["topic"] == topic
    ]


def create_question(word, words):
    correct_answer = word["translation"]

    options = [correct_answer]

    while len(options) < 4:
        random_word = random.choice(words)
        wrong_answer = random_word["translation"]

        if wrong_answer not in options:
            options.append(wrong_answer)

    random.shuffle(options)

    return options, correct_answer


def main():
    words = load_words()

    print("=== English Quiz ===")

    level = input("Choose level (A1/A2/B1/B2/C1/C2): ").upper()

    topic = input(
        "Choose topic (animals, food, travel, work, emotions): "
    ).lower()

    filtered_words = get_filtered_words(words, level, topic)

    if len(filtered_words) < 4:
        print("Not enough words for this category.")
        return

    random.shuffle(filtered_words)

    score = 0
    total_questions = min(10, len(filtered_words))

    for question_number in range(total_questions):

        word = filtered_words[question_number]

        options, correct_answer = create_question(
            word,
            filtered_words
        )

        print(f"\nQuestion {question_number + 1}")
        print(f"Translate: {word['word']}")

        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        answer = input("Your answer (1-4): ")

        if not answer.isdigit():
            print("Invalid input.")
            continue

        answer_index = int(answer) - 1

        if options[answer_index] == correct_answer:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong!")
            print(f"Correct answer: {correct_answer}")

    percentage = round(score / total_questions * 100)

    print("\n=== Results ===")
    print(f"Score: {score}/{total_questions}")
    print(f"Percentage: {percentage}%")

    scores = load_scores()

    scores["games_played"] += 1

    if percentage > scores["best_score"]:
        scores["best_score"] = percentage

    save_scores(scores)

    print(f"Games played: {scores['games_played']}")
    print(f"Best score: {scores['best_score']}%")


if __name__ == "__main__":
    main()
