import unittest

def is_valid_parenthesis(s: str) -> bool:
    possible_parenthesis = {'(': ')', '[': ']', '{':'}'}
    parenthesis_stack = []
    for char in s:
        if char in possible_parenthesis:
            parenthesis_stack.append(char)
        else:
            if not parenthesis_stack:
                return False
            val = parenthesis_stack.pop()
            if char != possible_parenthesis[val]:
                return False    
    return not parenthesis_stack



class TestIsValidParenthesis(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(is_valid_parenthesis(""))

    def test_basico(self):
        self.assertTrue(is_valid_parenthesis("()"))
        self.assertTrue(is_valid_parenthesis("[]"))
        self.assertTrue(is_valid_parenthesis("{}"))

    def test_contrario(self):
        self.assertTrue(is_valid_parenthesis("({[]})"))

    def test_mischiato(self):
        self.assertTrue(is_valid_parenthesis("()[]{}"))

    def test_ordinesbagliato(self):
        self.assertFalse(is_valid_parenthesis("(]"))
        self.assertFalse(is_valid_parenthesis("([)]"))

    def test_soloaperta(self):
        self.assertFalse(is_valid_parenthesis("("))
        self.assertFalse(is_valid_parenthesis("["))
        self.assertFalse(is_valid_parenthesis("{"))

    def test_solochiusa(self):
        self.assertFalse(is_valid_parenthesis(")"))
        self.assertFalse(is_valid_parenthesis("]"))
        self.assertFalse(is_valid_parenthesis("}"))

    def test_apertainpiu(self):
        self.assertFalse(is_valid_parenthesis("((())"))
        self.assertFalse(is_valid_parenthesis("([)"))
        self.assertFalse(is_valid_parenthesis("{[()]"))

    def test_chiusainpiu(self):
        self.assertFalse(is_valid_parenthesis("(()))"))
        self.assertFalse(is_valid_parenthesis("[]]"))
        self.assertFalse(is_valid_parenthesis("{{}}}"))

    def test_giusto(self):
        self.assertTrue(is_valid_parenthesis("({[(){}]})"))

if __name__ == '__main__':
    unittest.main()