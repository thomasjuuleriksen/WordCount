from unittest import TestCase
import functions


class My_searchandadd_TestCases(TestCase):
    def test_new_words_at_start(self):
        words = functions.WordCount()
        wordlist = ["first", "echo", "delta", "charlie", "bravo", "alpha"]
        expected_result = [{"word": "alpha", "count": 1}, {"word": "bravo", "count": 1}, {"word": "charlie", "count": 1}, {"word": "delta", "count": 1}, {"word": "echo", "count": 1}, {"word": "first", "count": 1}]
        for i in range(len(wordlist)):
            words.searchandadd(wordlist[i])
        self.assertEqual(words.wordcountlist, expected_result)

    def test_new_words_at_end(self):
        words = functions.WordCount()
        wordlist = ["first", "alpha", "bravo", "charlie", "delta",  "echo"]
        expected_result = [{"word": "alpha", "count": 1}, {"word": "bravo", "count": 1}, {"word": "charlie", "count": 1}, {"word": "delta", "count": 1}, {"word": "echo", "count": 1}, {"word": "first", "count": 1}]
        for i in range(len(wordlist)):
            words.searchandadd(wordlist[i])
        self.assertEqual(words.wordcountlist, expected_result)

    def test_same_words(self):
        words = functions.WordCount()
        wordlist = ["alpha" for _ in range(10000)] + ["first"]
        expected_result = [{"word": "alpha", "count": 10000}, {"word": "first", "count": 1}]
        for i in range(len(wordlist)):
            words.searchandadd(wordlist[i])
        self.assertEqual(words.wordcountlist, expected_result)

    def test_same_prefix(self):
        words = functions.WordCount()
        wordlist = ["first", "alpha", "alphamale", "alphabet", "alphabase", "alphart"]
        expected_result = [{"word": "alpha", "count": 1}, {"word": "alphabase", "count": 1}, {"word": "alphabet", "count": 1}, {"word": "alphamale", "count": 1}, {"word": "alphart", "count": 1}, {"word": "first", "count": 1}]
        for i in range(len(wordlist)):
            words.searchandadd(wordlist[i])
        self.assertEqual(words.wordcountlist, expected_result)

    def test_new_most_frequent(self):
        words = functions.WordCount()
        wordlist = ["first", "first", "we", "take", "Manhattan", "then", "we", "take", "Berlin", "with", "take", "that"]
        exp_res_unsorted = [{"word": "Berlin", "count": 1}, {"word": "Manhattan", "count": 1}, {"word": "first", "count": 2}, {"word": "take", "count": 3}, {"word": "that", "count": 1}, {"word": "then", "count": 1}, {"word": "we", "count": 2}, {"word": "with", "count": 1}]
        exp_res_sorted = [{"word": "take", "count": 3}, {"word": "first", "count": 2}, {"word": "we", "count": 2}, {"word": "Berlin", "count": 1}, {"word": "Manhattan", "count": 1},{"word": "that", "count": 1}, {"word": "then", "count": 1}, {"word": "with", "count": 1}]
        for i in range(len(wordlist)):
            words.searchandadd(wordlist[i])
        self.assertEqual((words.wordcountlist, words.sort()), (exp_res_unsorted, exp_res_sorted))

class My_processbuffer_TestCases(TestCase):
    def test_two_words_with_space(self):
        words = functions.WordCount()
        buffer = b'abc\tdef\r\n ghi    1234\r\n'
        expected_result = [{"word": "1234", "count": 1}, {"word": "abc", "count": 1}, {"word": "def", "count": 1},
                           {"word": "ghi", "count": 1}]
        words.processbuffer(buffer)
        self.assertEqual(words.wordcountlist, expected_result)

    def test_spaces_and_a_letter(self):
        words = functions.WordCount()
        buffer = b'    \t  \n          a\r'
        expected_result = "a"
        words.processbuffer(buffer)
        self.assertEqual(words.wordcountlist[0]["word"], expected_result)

    def test_word_at_end(self):
        words = functions.WordCount()
        buffer = b'1234   5678\r\n\r\n\r\n9ABC DEF\tabc	defghi    1234'
        expected_result = ([{'count': 1, 'word': '1234'}, {'count': 1, 'word': '5678'}, {'count': 1, 'word': '9abc'},
                            {'count': 1, 'word': 'abc'}, {'count': 1, 'word': 'def'}, {'count': 1, 'word': 'defghi'}],
                           "1234")
        words.processbuffer(buffer)
        self.assertEqual((words.wordcountlist, words.curr_word), expected_result)

if __name__ == '__main__':
    main()
