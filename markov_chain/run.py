from markov_python.cc_markov import MarkovChain
import urllib2

mc = MarkovChain()
response = urllib2.urlopen('http://www.gutenberg.org/cache/epub/30568/pg30568.txt')
html = response.read()
mc.add_string(html)

phrase1 = mc.generate_text()
phrase2 = mc.generate_text()
phrase3 = mc.generate_text()


def print_phrases(phrase):
    for words in phrase[0::3]:
        print words,
    print ""

print_phrases(phrase1)
print_phrases(phrase2)
print_phrases(phrase3)
