import unittest

from src.q02 import verify_password


class VerifyPasswordTest(unittest.TestCase):
    def testVerifyPassword_WithFourLowercaseLetters(self):
        expected = ['Deve possuir no mínimo 6 caracteres.', 'Deve conter no mínimo 1 número.', 'Deve conter no mínimo 1 letra maiúscula.', 'Deve conter no mínimo 1 caractere especial.']
        result = verify_password('jaci')
        self.assertEqual(expected, result)

    def testVerifyPassword_WithFourUppercaseLetters(self):
        expected = ['Deve possuir no mínimo 6 caracteres.', 'Deve conter no mínimo 1 número.', 'Deve conter no mínimo 1 letra minúscula.', 'Deve conter no mínimo 1 caractere especial.']
        result = verify_password('JACI')
        self.assertEqual(expected, result)

    def testVerifyPassword_WithFourNumbers(self):
        expected = ['Deve possuir no mínimo 6 caracteres.', 'Deve conter no mínimo 1 letra minúscula.', 'Deve conter no mínimo 1 letra maiúscula.', 'Deve conter no mínimo 1 caractere especial.']
        result = verify_password('7061')
        self.assertEqual(expected, result)

    def testVerifyPassword_WithFourSpecialCharacters(self):
        expected = ['Deve possuir no mínimo 6 caracteres.', 'Deve conter no mínimo 1 número.', 'Deve conter no mínimo 1 letra minúscula.', 'Deve conter no mínimo 1 letra maiúscula.']
        result = verify_password(')@(!')
        self.assertEqual(expected, result)

    def testVerifyPassword_WithSixLowercaseLetters(self):
        expected = ['Deve conter no mínimo 1 número.', 'Deve conter no mínimo 1 letra maiúscula.', 'Deve conter no mínimo 1 caractere especial.']
        result = verify_password('santos')
        self.assertEqual(expected, result)

    def testVerifyPassword_WithSixUppercaseLetters(self):
        expected = ['Deve conter no mínimo 1 número.', 'Deve conter no mínimo 1 letra minúscula.', 'Deve conter no mínimo 1 caractere especial.']
        result = verify_password('SANTOS')
        self.assertEqual(expected, result)

    def testVerifyPassword_WithSixNumbers(self):
        expected = ['Deve conter no mínimo 1 letra minúscula.', 'Deve conter no mínimo 1 letra maiúscula.', 'Deve conter no mínimo 1 caractere especial.']
        result = verify_password('502705')
        self.assertEqual(expected, result)

    def testVerifyPassword_WithSixSpecialCharacters(self):
        expected = ['Deve conter no mínimo 1 número.', 'Deve conter no mínimo 1 letra minúscula.', 'Deve conter no mínimo 1 letra maiúscula.']
        result = verify_password('$@#%@$')
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
