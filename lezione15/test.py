import unittest

def anagram(s: str, t: str) -> bool:
    return sorted(s.lower()) == sorted(t.lower())

class TestAnagramFunction(unittest.TestCase):
    def classico(self):
        self.assertTrue(anagram("listen", "silent"))
        self.assertTrue(anagram("triangle", "integral"))
        self.assertTrue(anagram("anagram", "nagaram"))
        self.assertTrue(anagram("Eleven plus two", "Twelve plus one"))

    def no_anagrammi(self):
        self.assertFalse(anagram("hello", "world"))
        self.assertFalse(anagram("python", "java"))
        self.assertFalse(anagram("apple", "pale"))
        self.assertFalse(anagram("rat", "car"))

    def lunghezze_diverse(self):
        self.assertFalse(anagram("a", "ab"))
        self.assertFalse(anagram("abc", "abcd"))
        self.assertFalse(anagram("123", "1234"))

    def stringhe_vuote(self):
        self.assertTrue(anagram("", ""))
        self.assertFalse(anagram("", "a"))
        self.assertFalse(anagram("a", ""))

    def sensibilita(self):
        self.assertTrue(anagram("Dormitory", "Dirty room"))
        self.assertTrue(anagram("Schoolmaster", "The classroom"))
        self.assertTrue(anagram("Astronomer", "Moon starer"))

    def caratteri_speciali(self):
        self.assertTrue(anagram("A man, a plan, a canal, Panama", "A plan, a canal, Panama, a man"))
        self.assertTrue(anagram("!@#$", "$#@!"))
        self.assertFalse(anagram("Hello, world!", "Hello world"))

if __name__ == '__main__':
    unittest.main()
