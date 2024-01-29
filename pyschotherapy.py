'''
Author: Elijah
Program: doctor.py
Chapter 5
01/10/2024

Conducts an interactive session of non-directive psychotherapy

'''
import random

# Global variables of various lists of data that all functions can share
hedges = ('Please, tell me more.', 'Many of my patients tell me the same thing.', 'Please, continue.', 'Go on, go on', "You don't say...")
qualifiers = ('Why do you say that ', 'You seem to think that ', 'Can you explain why ')
replacements = {'I': 'you', 'me': 'you', 'my': 'your', 'we': 'you', 'us': 'you', 'mine': 'yours', 'am': 'are', 'you': 'I'}

history = []

# Definition of the reply() function
def reply(sentence):
    # Builds and returns a reply to the user input.
    probability = random.randint(1, 6)
    if probability == 1:
        return random.choice(hedges)
    elif probability == 2 and len(history) > 3:
        return 'Earlier you told me that ' + random.choice(history)
    elif probability == 3:
        return 'How does that make you feel?'
    elif probability == 4:
        return 'Tell me more about your feelings.'
    elif probability == 5:
        return 'I am here to help. What else would you like to discuss?'
    else:
        return random.choice(qualifiers) + changePerson(sentence)

# Definition of the changePerson() function
def changePerson(sentence):
    # Replaces first person pronouns with second person pronouns
    words = sentence.split()
    replyWords = []
    for word in words:
        replyWords.append(replacements.get(word, word))

    response = ' '.join(replyWords)
    history.append(response)

    return response

# Definition of the main() function
def main():
    # Handles the interaction between user and doctor.
    print('Good Morning, I hope you are well today.')
    print('What can I do for you?')
    while True:
        sentence = input('\nType your response or QUIT to exit >> ')
        if sentence.upper() == 'QUIT':
            input('Have a great day! Press ENTER to close window >> ')
            break

        print(reply(sentence))

# Global call to main() for program execution
if __name__ == '__main__':
    main()
