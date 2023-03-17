from khaddoc_engine.specs_parser import get_specs_from_file

from khaddock_sailor.kernel import KernelParameter

def run():
    example_spec = get_specs_from_file('examples/vm.yaml')
    print(example_spec.specs.sysctl)

    kcmd = KernelParameter(kernel_parameters=example_spec.specs.sysctl)
    kcmd.run()


if __name__ == "__main__":
    run()