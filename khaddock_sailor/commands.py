import abc
import subprocess

class Command(abc.ABC):

    def __init__(self, requires_root: bool) -> None:
        super().__init__()
        self.requires_root = requires_root

    def become_root(self):
        print("Hello there")
        subprocess.run(["/usr/bin/bash", "-c", "sudo -u root"])

    @abc.abstractmethod
    def run(self) -> None:
        ...
