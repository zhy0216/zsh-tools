from collections import OrderedDict
import os
import sys
import shutil
import time

class Command:
    def __init__(self, raw_line: str):
        self.time, self.command = raw_line.split(";", 1)
        self.command = self.command.strip()

    def __hash__(self):
        return hash(self.command)

    def __eq__(self, other):
        return self.command == other.command

    def __repr__(self):
        return f"{self.time};{self.command}"



if __name__ == "__main__":
    zsh_history_path = os.path.expanduser('~/.zsh_history')
    if len(sys.argv) == 2:
        zsh_history_path = sys.argv[1]

    shutil.copy(zsh_history_path, f"{zsh_history_path}.{int(time.time())}")
    r = OrderedDict()
    with open(zsh_history_path, 'rb') as f:
        for line in f:
            full_line = line.decode('latin-1')
            while full_line.strip()[-1] == '\\':
                full_line += next(f).decode('latin-1')

            r[Command(full_line)] = None

    with open(zsh_history_path, 'w') as f:
        f.write(os.linesep.join(map(str, r.keys())))





