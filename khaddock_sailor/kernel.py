import subprocess

from khaddock_sailor.commands import Command, WithPriviledge


class KernelParameter(Command):

    def __init__(self, kernel_parameters: dict[str, str | int]) -> None:
        super().__init__(priviledged=True)
        self.kernel_parameters = kernel_parameters

    def run(self) -> None:
        # Run the next commands as priviledged.
        with WithPriviledge():
            for k, v in self.kernel_parameters.items():
                parameter_path = '/'.join(k.split('.'))
                process = subprocess.run(
                    f'echo {v} | sudo tee /proc/sys/{parameter_path}',
                    stdout=subprocess.DEVNULL,
                    shell=True
                )
                process.check_returncode()
