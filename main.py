train_data = [
    ("I got full marks in the test today!", "Happy"),
    ("We won the college cricket match", "Happy"),
    ("My friends planned a surprise party for me", "Happy"),
    ("The food in the canteen was really tasty", "Happy"),
    ("I am so excited for the weekend trip", "Happy"),
    ("Our project got selected for the exhibition", "Happy"),
    ("I finally learned how to ride a bicycle", "Happy"),
    ("Mom made my favourite sweets today", "Happy"),
    ("I lost my phone on the bus", "Sad"),
    ("I failed in the mathematics exam", "Sad"),
    ("My best friend is moving to another city", "Sad"),
    ("It rained and our picnic was cancelled", "Sad"),
    ("I missed the last bus and felt very upset", "Sad"),
    ("My laptop stopped working before the submission", "Sad"),
    ("I felt lonely during the long holidays", "Sad")
]
def count_moods(data):

    happy = 0
    sad = 0

    for sentence, mood in data:

        if mood == "Happy":
            happy = happy + 1

        elif mood == "Sad":
            sad = sad + 1

    return (happy, sad)
print("Level 1 - Mood Count:")
print(count_moods(train_data))
happy_words = ["won", "surprise", "excited"]

sad_words = ["lost", "failed", "lonely"]
def guess_mood(sentence):

    sentence = sentence.lower()

    cleaned_sentence = ""

    for character in sentence:

        if character.isalpha() or character.isspace():
            cleaned_sentence = cleaned_sentence + character

    words = cleaned_sentence.split()

    happy_count = 0
    sad_count = 0

    for word in words:

        if word in happy_words:
            happy_count = happy_count + 1

        if word in sad_words:
            sad_count = sad_count + 1

    if happy_count > sad_count:
        return "Happy"

    else:
        return "Sad"

practice_data = [
    ("I won a medal in the sports meet", "Happy"),
    ("I lost my notebook before the exam", "Sad"),
    ("My friends gave me a lovely surprise", "Happy"),
    ("The train was late and I felt upset", "Sad"),
    ("Today was a great day", "Happy")
]
correct = 0

print("\nLevel 3 - Testing Results:")

for sentence, actual_mood in practice_data:

    predicted_mood = guess_mood(sentence)

    print("Sentence:", sentence)
    print("Actual Mood:", actual_mood)
    print("Predicted Mood:", predicted_mood)
    print()

    if predicted_mood == actual_mood:
        correct = correct + 1

total = len(practice_data)

accuracy = (correct / total) * 100

print("Correct Predictions:", correct)
print("Total Sentences:", total)
print("Accuracy:", accuracy, "%")
