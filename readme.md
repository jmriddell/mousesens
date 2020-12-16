# Mousesens

Simple command line utility to change the sensitivity of a pointer device under linux using the `xinput` command.

## Reason

* Minimal systems like Archlinux installations don't come with any graphical or text-based utility to do this.
* Many utilities come as a part of a desktop environment, and may not work properly if used not in its respective desktop environment.
* Many utilities can adjust just the acceleration of the pointer device instead of the pixels per physical distance relation.
* Doing this task using `xinput` alone requires entering a very long line into the terminal with repeated info, which is far from ideal if trying different settings to find the right one.
* There are many articles available online on how to change the mouse acceleration, but what we usually want to adjust is just the linear speed of the pointer device.

## Features

* Command line completion.
* Per device setting.

## Caveats

* Settings are not persistent, for persistent settings it can be called in a startup script.

## Installation

1. Download and install
    * If you don't have git installed
       ```bash
       pip install https://github.com/jmriddell/mousesens/archive/master.zip
       ```
    * If you have git installed:
       ```bash
       pip install git+https://github.com/jmriddell/mousesens.git
       ```
    In both cases can be done appending the option `--user` to avoid requiring root privileges.

2. Activate shell completion (optional)

    The procedure will vary slightly depending on your shell:

    * For Bash, add this to `~/.bashrc`:
        ```bash
        eval "$(_MOUSESENS_COMPLETE=source_bash mousesens)"
        ```
    * For Zsh, add this to `~/.zshrc`:
        ```bash
        eval "$(_MOUSESENS_COMPLETE=source_zsh mousesens)"
        ```
    * For Fish, add this to `~/.config/fish/completions/mousesens.fish`:
        ```bash
        eval (env _MOUSESENS_COMPLETE=source_fish mousesens)
        ```


## Usage

It has two subcommands:

### `list`

Show pointer devices names.

```bash
mousesens list
```


### `set`

Set the sensitivity of a pointer device given its name and a sensitivity value.

```bash
mousesens set [DEVICE_NAME] [SENSITIVITY]
```

Examples:
```bash
mousesens set "SynPS/2 Synaptics TouchPad" 0.25
mousesens set "SynPS/2 Synaptics TouchPad" 6
mousesens set SynPS/2\ Synaptics\ TouchPad 6
```
