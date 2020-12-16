"""Interface with xinput functionality."""

import subprocess


def _get_name(line):
    """Get name of a pointer device given it's line from 'xinput --list'."""
    return line[6:].split("\t", maxsplit=1)[0].rstrip()


def get_pointer_devices():
    """Get a list of pointer device names using 'xinput --list'."""
    string = subprocess.run(
        ["xinput", "list"],
        capture_output=True,
        encoding="utf8"
    ).stdout

    return list(
        filter(lambda x: x != "Virtual core XTEST pointer",
            map(
                _get_name,
                filter(
                    lambda x: x.startswith('⎜'),
                    string.splitlines()
                )
            )
        )
    )


def _mousesens_command(device:str, sensitivity:float):
    """Make the command to be executed to change the pointer sensitivity."""
    sens_string = format(sensitivity, 'f')
    return [
        'xinput',
        'set-prop',
        device,
        'Coordinate Transformation Matrix',
        sens_string + ',',
        '0.000000,',
        '0.000000,',
        '0.000000,',
        sens_string + ',',
        '0.000000,',
        '0.000000,',
        '0.000000,',
        '1.000000'
    ]

def set_sensitivity(device:str, sensitivity:float):
    """Set the sensitivity of a pointer device."""
    subprocess.run(_mousesens_command(device, sensitivity),)
