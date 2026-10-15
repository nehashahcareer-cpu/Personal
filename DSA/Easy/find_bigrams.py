
def find_bigrams(sentence):
    """
    Return all consecutive word pairs (bigrams) from a sentence.

    The function converts the sentence to lowercase, splits it into words,
    and creates pairs of adjacent words in their original order.

    Args:
        sentence (str): A sentence or paragraph containing words.

    Returns:
        list[tuple[str, str]]: A list of consecutive word pairs.
        Returns an empty list if the sentence contains fewer than two words.

    Time Complexity:
        O(c), where c is the number of characters in the sentence.
        Lowercasing and splitting process the input, and creating bigrams
        takes O(w), where w is the number of words.

    Auxiliary Space Complexity:
        O(w), where w is the number of words.
        The words list and the resulting bigram list require additional space.
    """

    # Step 1: Convert the sentence to lowercase and split it into words.
    words = sentence.lower().split()

    # Step 2: Initialize an empty list to store consecutive word pairs.
    result = []

    # Step 3: Start at index 1 because each pair uses the current word
    # and the previous word.
    for i in range(1, len(words)):

        # Step 4: Add the previous word and current word as a tuple.
        result.append((words[i - 1], words[i]))

    # Step 5: Return the list of all consecutive word pairs.
    return result


if __name__ == "__main__":
    # Test 1: Normal sentence
    sentence1 = "Have free time to drive children?"
    print(find_bigrams(sentence1))
    # [('have', 'free'), ('free', 'time'), ('time', 'to'),
    #  ('to', 'drive'), ('drive', 'children?')]

    # Test 2: Empty sentence
    sentence2 = ""
    print(find_bigrams(sentence2))
    # []

    # Test 3: Sentence with only one word
    sentence3 = "Hello"
    print(find_bigrams(sentence3))
    # []

    # Test 4: Mixed uppercase and lowercase
    sentence4 = "Python IS fun"
    print(find_bigrams(sentence4))
    # [('python', 'is'), ('is', 'fun')]

    # Test 5: Multiple spaces and line breaks
    sentence5 = "Hello   world\nHow are you?"
    print(find_bigrams(sentence5))
    # [('hello', 'world'), ('world', 'how'),
    #  ('how', 'are'), ('are', 'you?')]
