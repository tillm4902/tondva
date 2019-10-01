import random
from typing import Dict, IO, Mapping, List
from collections import Counter

class User:
    """
    Docstring?

    === Private Attributes ===
    start:
    words:
    lengths:
    """
    start: Mapping[str, int]
    words: Dict[str, List[Mapping[str, int], Mapping[str, int]]]
    lengths: Mapping[int, int]

    def __init__(self) -> None:
        self.start = Counter()
        self.words = {}
        self.lengths = Counter()

class MessageGenerator:
    """
    Docstring goes here

    === Private Attributes ===
    _users: word_frequency dict for all users
    """
    _users: Dict[str, User]

    def __init__(self) -> None:
        """
        Docstrings are for puccis
        """
        self._users = {'everyone':User(),
        'Pikalover208#1521':User(),
        'Meepithmancer#1949':User(),
        'Triblendlightning#8681':User(),
        'Yreid#3772':User(),
        'archiem#9414':User(),
        'ads3500#5349':User(),
        'iain_theginger#3818':User()}

    def append_words(self,user:str, word:str,
                     last:Union[str, None], laster:Union[str, None]) -> None:
        """
        Dab on the developers
        """
        if last == None:
            self._users[user].start[word] += 1
            self._users['everyone'].start[word] += 1
        else:
            if last not in self._users[user].words.keys():
                self._users[user].words[last] = [Counter(), Counter()]
            if last not in self._users['everyone'].words.keys():
                self._users['everyone'].words[last] = [Counter(), Counter()]
            # TODO Finish this shit
            self._users[user].words[last][0][word] += 1
            self.


    def import_msgs(self, source:IO[str]) -> None:
        """
        lmao imagine actually being a good developer
        """
        source.readline()
        for message in source:
            words = message.split()
            user = words[0]

            if user in self._users.keys():
                last_word = str(words[1])

                self._users[user].start[last_word] += 1
                self._users[user].lengths[len(words[1:])] += 1

                self._users['everyone'].start[last_word] += 1
                self._users['everyone'].lengths[len(words[1:])] += 1

                if last_word not in self._users[user].words.keys():
                    self._users[user].words[last_word] = Counter()

                if last_word not in self._users['everyone'].words.keys():
                    self._users['everyone'].words[last_word] = Counter()

                if len(words) > 2:
                    for word in words[2:]:
                        if word not in self._users[user].words.keys():
                            self._users[user].words[word] = Counter()
                        self._users[user].words[last_word][word] += 1

                        if word not in self._users['everyone'].words.keys():
                            self._users['everyone'].words[word] = Counter()
                        self._users['everyone'].words[last_word][word] += 1

                        last_word = word

        source.close()

    def export_data(self) -> None:
        """
        Yup that right there's a docstring
        """
        #TODO Maybe implement this method
        pass


    def generate_message(self, user = 'everyone',
                         length = random.choice(list(self._users[user].lengths.elements())),
                         word = random.choice(list(self._users[user].start.elements()))) -> str:
        """
        D O C S T R I N G
        """
        punctuation = ['.','!','?']
        message = word

        for i in range(length-1):
            while len(list(self._users[user].words[word].elements())) == 0:
                word = random.choice(list(self._users[user].start.elements()))
                message += (" " + word)
            next_word = random.choice(list(self._users[user].words[word].elements()))
            message += (" " + next_word)
            word = next_word

        return message
