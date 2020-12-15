"""Change the mouse sensibility."""

import click
import subprocess
import mousesens.xinput_interface as xi


@click.group()
def cli():
    """Command line utility to change the sensibility of a pointer device."""
    pass


@click.command(name="set")
@click.argument(
    "device", type=click.Choice(xi.get_pointer_devices())
)
@click.argument("sensibility", type=click.FLOAT)
def set_sensibility(device, sensibility):
    """Set the sensibility of a pointer device."""
    xi.set_sensibility(device, float(sensibility))


@click.command(name="list")
def list_devices():
    """List available pointer devices."""
    devices = xi.get_pointer_devices()

    for device in devices:
        click.echo(message=device)


cli.add_command(list_devices)
cli.add_command(set_sensibility)
