"""Change the mouse sensibility."""

import click
import subprocess


def get_name(line):
    """Get name of a pointer device given it's line from 'xinput --list'."""
    return line[6:].split("\t", maxsplit=1)[0].rstrip()


def get_pointer_devices():
    """Get a list of pointer device names using 'xinput --list'."""
    string = subprocess.run(
        ["xinput", "--list"],
        capture_output=True,
        encoding="utf8"
    ).stdout

    return list(
        map(
            get_name,
            filter(
                lambda x: x.startswith('⎜'),
                string.splitlines()
            )
        )
    )


def mousesens_command(device, sensibility):
    """Make the command to be executed to change the pointer sensibility."""
    sens_string = format(sensibility, 'f')
    return [
        'xinput',
        '--set-prop',
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


@click.group()
def cli():
    """Command line utility to change the sensibility of a pointer device."""
    pass


@click.command(name="set")
@click.argument(
    "device", type=click.Choice(get_pointer_devices())
)
@click.argument("sensibility", type=click.FLOAT)
def set_sensibility(device, sensibility):
    """Set the sensibility of a pointer device."""
    subprocess.run(mousesens_command(device, float(sensibility)),)


@click.command(name="list")
def list_devices():
    """List available pointer devices."""
    devices = get_pointer_devices()

    for device in devices:
        click.echo(message=device)


cli.add_command(list_devices)
cli.add_command(set_sensibility)
