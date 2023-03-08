import subprocess

from khaddock_sailor.commands import Command

class SysCtlCommand(Command):

    def __init__(self, sysctl_specs: dict[str, str | int]) -> None:
        super().__init__(requires_root=True)
        self._sysctl_specs = sysctl_specs

    def _sysctl_cmd() -> None:
        pass

    def run(self) -> None:

        with sh.contrib.sudo:
            sh.sysctl('-w', f'fs.inotify.max_user_instances=128')

        # with open('/etc/sysctl.conf', 'a') as f:
        # for k, v in self._sysctl_specs.items():
        #     proc = subprocess.run(["/usr/bin/bash", "-c", f"sysctl -w {k}={v}"], preexec_fn=self.become_root)
        #     proc.check_returncode()