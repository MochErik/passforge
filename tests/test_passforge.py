"""Unit tests for PassForge."""

import unittest
from passforge.generator import generate_password, generate_passphrase, generate_token, calculate_entropy


class TestPassForge(unittest.TestCase):

    def test_password_length_and_entropy(self):
        res = generate_password(length=20)
        self.assertEqual(len(res["password"]), 20)
        self.assertGreater(res["entropy_bits"], 70)
        self.assertEqual(res["strength"], "Very Strong")

    def test_passphrase_generation(self):
        res = generate_passphrase(word_count=4)
        self.assertEqual(res["words"], 4)
        self.assertIn("-", res["passphrase"])

    def test_token_length(self):
        token = generate_token(bytes_len=16, encoding="hex")
        self.assertEqual(len(token), 32)


if __name__ == "__main__":
    unittest.main()
