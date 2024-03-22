"""


"""
def findSecretWord(words, master, allowedGuesses):
    def calc_similarity(w1, w2):
        return sum(c1 == c2 for c1, c2 in zip(w1, w2))

    def filter_words(words, guess, matches):
        return [word for word in words if calc_similarity(word, guess) == matches]

    guess = words[0]
    while allowedGuesses > 0:
        matches = master.guess(guess)
        if matches == 6:
            return "You guessed the secret word correctly."
        words = filter_words(words, guess, matches)
        guess = words[0] if len(words) > 0 else words[0]  # Choose the first word if available
        allowedGuesses -= 1

    return "Either you took too many guesses, or you did not find the secret word."

# Example usage
class Master:
    secret_word = "python" 

    def guess(self, word):
        if word not in words:
            return -1
        return sum(c1 == c2 for c1, c2 in zip(word, self.secret_word))

words = ["puzzle", "python", "guitar", "rocket", "planet"]  # Example list of words
allowedGuesses = 5

result = findSecretWord(words, Master(), allowedGuesses)
print(result)