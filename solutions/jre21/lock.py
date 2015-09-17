import re

lock = ['BDMJPRSTLN', 'AEIOUYRTLH', 'ACDEORSTLN', 'DHKYRSTLNE']

words = set()

# Create a hash table of all four-letter words which use only standard
# (unaccented) characters.
with open('/usr/share/dict/words', 'r') as f:
    word = f.readline()
    while (word):
        word = word.strip().upper()
        if re.match('^[A-Z]{4}$', word):
            words.add(word)
        word = f.readline()

solutions = []

# Iterate through all possible positions of the bottom three reels
# relative to the top reel.  Then, for each position, enumerate the
# columns which form real words.  Save all sets of 3+ words.
for second in range(len(lock[1])):
    for third in range(len(lock[2])):
        for fourth in range(len(lock[3])):
            found = []
            for index in range(len(lock[0])):
                word = ''.join([
                                lock[0][index],
                                lock[1][(second+index)%len(lock[1])],
                                lock[2][(third+index)%len(lock[2])],
                                lock[3][(fourth+index)%len(lock[3])]
                                ])
                if word in words:
                    found.append(word)
            if len(found) >= 3:
                found.sort()
                solutions.append(tuple(found))

# Print the solutions, alphabetized by first word.
solutions = list(set(solutions))
solutions.sort(key=lambda x: x[0])
for solution in solutions:
    print(solution)

# Print in alphabetical order all words which appear in a triplet.
answers = list(set([x for y in solutions for x in y]))
answers.sort()
print(answers)
