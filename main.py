from khaddoc_engine.specs import KhaddockMetadata
from khaddoc_engine.specs_parser import get_specs_from_file

from khaddock_sailor.sysctl import SysCtlCommand

def run():
    a = get_specs_from_file('examples/vm.yaml')
    # TODO: later
    # b = get_commands_from_specs(a)
    print(a.specs.sysctl)

    sysctl_cmd = SysCtlCommand(sysctl_specs=a.specs.sysctl)
    sysctl_cmd.run()


if __name__ == "__main__":
    run()