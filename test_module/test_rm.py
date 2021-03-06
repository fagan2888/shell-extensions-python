
import unittest

from shell_extensions_python import mkdir, rm, symlink, ls, write, CannotRemoveDirectoryError, r
from shell_extensions_python.interactive import Interactive

from .utilities import reset

class TestRm(unittest.TestCase):
    @reset
    def test_rm_dne(self):
        self.assertRaises(FileNotFoundError, lambda: rm('does-not-exist'))
        rm('does-not-exist', ignore_missing=True)
    @reset
    def test_rmdir(self):
        mkdir('empty-folder')
        rm('empty-folder')
        self.assertEqual([], ls())
    @reset
    def test_rm_nonemptydir(self):
        mkdir('path')
        write('path/file', 'contents')
        self.assertRaises(CannotRemoveDirectoryError, lambda: rm('path', interactive=False))
        self.assertEqual(['path'], ls())
        rm('path', recursively=True)
        self.assertEqual([], ls())
        mkdir('path')
        write('path/file', '')
        Interactive.ask_question = lambda _: "n"
        rm('path')
        self.assertEqual(['path'], ls())
        Interactive.ask_question = lambda _: "y"
        rm("path")
        self.assertEqual([], ls())
    @reset
    def test_rm_symlink(self):
        write('file', 'contents')
        symlink('file', 'link')
        rm('link')
        self.assertEqual(['file'], ls())
        rm('file')
    @reset
    def test_rm_symlink_to_folder(self):
        mkdir('folder')
        symlink('folder', 'link')
        rm('link')
        self.assertEqual(['folder'], ls())
        rm('folder')
    @reset
    def test_rm_with_one_nonexistant(self):
        write('existant', 'contents')
        self.assertRaises(FileNotFoundError, lambda: rm('existant', 'nonexistant'))
        self.assertEqual(['existant'], ls())
        rm('existant', 'nonexistant', ignore_missing=True)
        self.assertEqual([], ls())
    @reset
    def test_rm_with_one_with_contents(self):
        write('existant', 'contents')
        mkdir('folder')
        write('folder/file', 'contents')
        self.assertRaises(CannotRemoveDirectoryError, lambda: rm('existant', 'folder', interactive=False))
        self.assertEqual(['existant', 'folder'], ls())
        rm('existant', 'folder', recursively=True)
        self.assertEqual([], ls())
