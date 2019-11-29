import emoji
import nltk


class SarcasmAnalysis:

    def __init__(self):
        self.sarcastic_emojis = [b'\xf0\x9f\x98\x8f', b'\xf0\x9f\x98\x90', b'\xf0\x9f\x99\x84', b'\xf0\x9f\xa4\xa8']
        self.adjectives_glossary = "C:\Himanshu\higher_adjectives.txt"  # config file
        self.char_repetitive_threshold = 3

    def extract_emojis(self, text):
        return ' '.join(c for c in text if c in emoji.UNICODE_EMOJI)

    def is_sarcastic_emoji(self, text):
        emoji_list = self.extract_emojis(text)
        if len(emoji_list) == 0:
            return None

        emoji_unicode_list = emoji_list.encode('utf-8').split()

        for emoji_unicode in emoji_unicode_list:
            if emoji_unicode in self.sarcastic_emojis:
                return True

    def extract_adjectives(self, text):
        try:
            adjective_grammar = r"""JJ: {<JJ|JJS|JJR>+} """
            adjective_regex_parser = nltk.RegexpParser(adjective_grammar)
            words = adjective_regex_parser.parse(nltk.pos_tag(nltk.word_tokenize(text)))

            adjectives_set = set()
            for tree in words.subtrees(filter=lambda t: t.label() == 'JJ'):
                adjectives_set.add(' '.join([child[0] for child in tree.leaves()]))

            return adjectives_set
        except Exception as e:  # use specific exception
            print(str(e))  # log

    def extract_verbs_adverbs(self, sentence):
        try:
            grammar = r"""vp : {<v|vb|vbd|rb|vbg>+}"""
            chunker = nltk.RegexpParser(grammar)
            chunk = chunker.parse(nltk.pos_tag(nltk.word_tokenize(sentence)))
            verbs_adverbs_set = set()
            for tree in chunk.subtrees(filter=lambda t: t.label() == 'vp'):
                verbs_adverbs_set.add(' '.join([child[0] for child in tree.leaves()]))
            return verbs_adverbs_set

        except Exception as e:
            print(str(e))

    def is_repetitive(self, words):
        for word in words:
            word_count = {}
            for char in word:
                if char in word_count:
                    word_count[char] += 1
                else:
                    word_count[char] = 1

            for char in word_count:
                if word_count[char] > self.char_repetitive_threshold:
                    print('is repetitive')
                    return True
                else:
                    return self.is_upper_style_case(char)

    def is_upper_style_case(self, word):
        # add bold, italics or underlined
        return word.isupper()

    def is_sarcastic_verb(self, text):
        verbs_set = self.extract_verbs_adverbs(text)
        if len(verbs_set) == 0:
            return None

        return self.is_repetitive(verbs_set)

    def is_higher_adjective(self, text):
        adjectives_set = self.extract_adjectives(text)
        if len(adjectives_set) == 0:
            return None

        file = open(self.adjectives_glossary, encoding='utf-8')
        text_adjectives_set = set()
        try:
            for line in file:
                words = line.strip().split('/n')
                for adjective in adjectives_set:
                    if adjective in words:
                        text_adjectives_set.add(adjective)

        except IOError as io:
            print(str(io))

        finally:
            file.close()

        if len(text_adjectives_set) == 0:
            return None

        return self.is_repetitive(self, text_adjectives_set)

    def process_tweets(self, tweets):
        for tweet in tweets:
            if self.is_sarcastic_emoji(tweet) is None:

                if self.is_higher_adjective(tweet) is None:
                    if self.is_sarcastic_verb(tweet) is None:
                        print("You are not sarcastic !!")
                else:
                    if self.is_higher_adjective(tweet):
                        print("You are sarcastic !!")
                    else:
                        print("You are not sarcastic !!")

            else:
                print("You are sarcastic !!")


