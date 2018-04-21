
The shell_extensions_python module is a module to be able to write shell scripts on python and use python as your shell.

It provides a number of commands.

## Drop-in replacements for Shell Utilities

 - `cd`: `cd()` takes you to `~`, `cd(path)` takes you to that relative path, and `cd(num)` takes you back `num` steps in your `cd` history.
 - `ls`: `ls(path='.')` returns a list of the contents of the given path, as a directory, sorted by default. Set `sort_key=None` in the call to not sort the results
 - `cat(path)`: reads the given file and returns it as a string. `cat(path, 'b')` reads the file as a binary sequence.
 - `write(path, contents)`: writes the given contents to the given file. By default does not overwrite existing files. `write(path, contents, clobber=True)` clobbers existing files, and `write(path, contents, append=True)` overwrites existing files.
 - `pwd()`: gets the current working directory
 - `rm(path)`: removes the given path if its a normal file. If it doesn't exist, it will error. To disable this effect, turn on the `ignore_missing=True` file. If it encounters a directory, it will prompt for whether or not it should be removed. To disable this effect so that it errors when it attempts to remove a directory, set `interactive=False`. To disable this so it removes the directory, set `recursively=True`.
