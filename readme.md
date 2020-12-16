# Mousesens

Simple command line utility to change the sensibility of a pointer device under linux using the `xinput` command.

## Reason

* Minimal systems like Archlinux installations don't come with any graphical or text-based utility to do this.
* Many utilities come as a part of a desktop environment, and may not work properly if used not in its respective desktop environment.
* Many utilities can adjust just the acceleration of the pointer device instead of the pixels per physical distance relation.
* Doing this task using `xinput` alone requires entering a very long line into the terminal with repeated info, which is far from ideal if trying different settings to find the right one.
* There are many articles available online show how to change the mouse acceleration, but what we usually want to adjust is just the linear speed of the pointer device.

## Features

* Command line completion.
* Per device setting.

## Caveats

* Settings are not persistent, for persistent settings it can be called in a startup script.

## Installation

1. To get a copy you can either:
    * Clone Github repository
        ```bash
        git clone https://github.com/jmriddell/mousesens.git
        ```
    * Download manually

2. Install
    1. Open a terminal and change to repository folder
    2. Once in the repository folder you can either:
        * Install using pip
            ```bash
            pip install .
            ```
        * Install running setup.py
            ```bash
            python setup.py install
            ```
        In both cases can be done appending the option `--user` to avoid requiring root privileges.

3. Activate shell completion (optional)

    The procedure will vary slightly depending on your shell:

    * For Bash, add this to `~/.bashrc`:
        ```bash
        eval "$(_FOO_BAR_COMPLETE=source_bash foo-bar)"
        ```
    * For Zsh, add this to `~/.zshrc`:
        ```bash
        eval "$(_FOO_BAR_COMPLETE=source_zsh foo-bar)"
        ```
    * For Fish, add this to `~/.config/fish/completions/foo-bar.fish`:
        ```bash
        eval (env _FOO_BAR_COMPLETE=source_fish foo-bar)
        ```


## Usage

It has two subcommands:

### `list`

Show pointer devices names.

```bash
mousesens list
```


### `set`

Set the sensibility of a pointer device given its name and a sensibility value.

```bash
mousesens set [DEVICE_NAME] [SENSIBILITY]
```

Examples:
```bash
mousesens set "SynPS/2 Synaptics TouchPad" 0.25
mousesens set "SynPS/2 Synaptics TouchPad" 6
mousesens set SynPS/2\ Synaptics\ TouchPad 6
```
