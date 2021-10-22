from unittest import TestCase
import os
import filehandling

class MyTestCase(TestCase):
    def test_file_does_not_exist(self):
        cwd = os.getcwd()
        try:
            os.remove(f"{cwd}\\bumkarl.txt")
        except FileNotFoundError:
            pass
        f = filehandling.FileHandling(f"{cwd}\\bumkarl.txt")
        self.assertEqual(f.file_ok, False)  # add assertion here

    def test_invalid_path(self):
        f = filehandling.FileHandling("C:\Program Files/Microsoft Office\Data\Delta\\root\habari.txt")
        self.assertEqual(f.file_ok, False)  # add assertion here

    def test_access_and_correct_size(self):
        cwd = os.getcwd()
        s = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do " \
            "eiusmod tempor incididunt ut labore et dolore magna aliqua."
        with open(f"{cwd}\\bumkarl.txt", "w") as inp:
            inp.write(s)
        f = filehandling.FileHandling(f"{cwd}\\bumkarl.txt")
        self.assertEqual((f.file_ok, f.file_size), (True, 123))  # add assertion here
        os.remove(f"{cwd}\\bumkarl.txt")

    def test_empty_file(self):
        cwd = os.getcwd()
        with open(f"{cwd}\\bumkarl.txt", "w") as inp:
            inp.write("")
        f = filehandling.FileHandling(f"{cwd}\\bumkarl.txt")
        b = f.readfromfile()
        self.assertEqual((f.file_ok, f.file_size, b), (True, 0, None))  # add assertion here
        os.remove(f"{cwd}\\bumkarl.txt")

    def test_wellformatted_file(self):
        cwd = os.getcwd()
        s = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do " \
            "eiusmod tempor incididunt ut labore et dolore magna aliqua."
        with open(f"{cwd}\\bumkarl.txt", "w") as inp:
            inp.write(s)
        f = filehandling.FileHandling(f"{cwd}\\bumkarl.txt")
        b1 = f.readfromfile(100)
        b2 = f.readfromfile(10)
        self.assertEqual((f.file_ok, f.file_size, b1, b2), (True, 123, b'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore ', b'et dolore '))  # add assertion here
        os.remove(f"{cwd}\\bumkarl.txt")

    def test_read_whole_file(self):
        cwd = os.getcwd()
        s = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do " \
            "eiusmod tempor incididunt ut labore et dolore magna aliqua."
        s1 = b'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do ' \
             b'eiusmod tempor incididunt ut labore '
        s2 = b'et dolore magna aliqua.'
        with open(f"{cwd}\\bumkarl.txt", "w") as inp:
            inp.write(s)
        f = filehandling.FileHandling(f"{cwd}\\bumkarl.txt")
        b1 = f.readfromfile(100)
        b2 = f.readfromfile(100)
        self.assertEqual((f.file_ok, f.file_size, b1, b2), (True, 123, s1, s2))  # add assertion here
        os.remove(f"{cwd}\\bumkarl.txt")

    def test_read_whole_file_in_one_chunk(self):
        cwd = os.getcwd()
        s = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do " \
            "eiusmod tempor incididunt ut labore et dolore magna aliqua."
        s1 = b'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do ' \
             b'eiusmod tempor incididunt ut labore et dolore magna aliqua.'
        with open(f"{cwd}\\bumkarl.txt", "w") as inp:
            inp.write(s)
        f = filehandling.FileHandling(f"{cwd}\\bumkarl.txt")
        b1 = f.readfromfile(123)
        b2 = f.readfromfile(123)
        self.assertEqual((f.file_ok, f.file_size, b1, b2), (True, 123, s1, None))  # add assertion here
        os.remove(f"{cwd}\\bumkarl.txt")


if __name__ == '__main__':
    main()
