import unittest
from unittest.mock import patch, mock_open
import main

class TestPlagiarismChecker(unittest.TestCase):
    def test_read_file_exists(self):
        with patch('builtins.open', mock_open(read_data='test data')):
            self.assertEqual(main.read_file('exists.txt'), 'test data')

    def test_read_file_not_exists(self):
        with patch('builtins.open', side_effect=FileNotFoundError):
            self.assertIsNone(main.read_file('nonexistent.txt'))

    def test_preprocess_text(self):
        self.assertEqual(main.preprocess_text('Hello, World!'), 'hello world')
        self.assertEqual(main.preprocess_text('123'), '123')
        self.assertEqual(main.preprocess_text(''), '')

    def test_calculate_similarity_identical(self):
        self.assertEqual(main.calculate_similarity('hello world', 'hello world'), 1.0)

    def test_calculate_similarity_different(self):
        self.assertAlmostEqual(main.calculate_similarity('hello', 'world'), 0.2, places=2)

    def test_calculate_similarity_with_special_chars(self):
        self.assertAlmostEqual(main.calculate_similarity('hello#world', 'hello world'), 0.909, places=2)

    @patch('sys.argv', ['script.py', 'original.txt', 'plagiarized.txt', 'output.txt'])
    def test_main_flow(self):
        with patch('builtins.print') as mocked_print:
            with patch('main.read_file', side_effect=['hello world', 'hello world', None]):
                with patch('main.calculate_similarity', return_value=1.0):
                    main.main()
                    mocked_print.assert_called_with("相似度计算完成，结果已写入 output.txt")

    @patch('sys.argv', ['script.py', 'original.txt', 'plagiarized.txt', 'output.txt'])
    def test_main_error_handling(self):
        with patch('main.read_file', side_effect=FileNotFoundError):
            with self.assertRaises(SystemExit):
                main.main()

if __name__ == '__main__':
    unittest.main()