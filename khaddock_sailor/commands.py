import abc
import subprocess

class Command(abc.ABC):

    def __init__(self, priviledged: bool) -> None:
        super().__init__()
        self.priviledged = priviledged

    @abc.abstractmethod
    def run(self) -> None:
        ...

class WithPriviledge:

    def __enter__(self):
        # Elevates the privileges for the next commands within the context.
        process = subprocess.run(
            ['sudo', '-S', 'echo', 'whatever'],
            stdout=subprocess.DEVNULL,
            universal_newlines=True
        )
        if process.returncode != 0:
            print('Error trying to get priviledged')
            exit(process.returncode)

    def __exit__(self, exc_type, exc_val, exc_tb):
        subprocess.run(['sudo', '-k'])
