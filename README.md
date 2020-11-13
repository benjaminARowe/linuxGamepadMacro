# linuxGamepadMacro

Linux gamepad macro is a small program for recording and playing gamepad macros on linux

## Requirements

I recommend using pipenv for dependancies. Install pipenv using your package manager e.g.

Debian / Ubuntu
```bash
sudo apt install pipenv
```

Fedora 
```bash
sudo dnf install pipenv
```

Arch 
```bash
sudo pacman -S python-pipenv
```

## Installation

Clone the repository

```bash
git clone https://github.com/benjaminARowe/linuxGamepadMacro
```

Change to the new dir

```bash
cd linuxGamepadMacro
```

Install the dependancies using pipenv

```bash
pipenv install 
```

## Usage

### Record a macro
```bash
pipenv run python read.py --file-name example.json
```
Then press a button on the gamepad you wish to use to select it. You can then start recording the macro

### Play a macro
```bash
pipenv run python run.py --file-name example.json
```
Then press a button on the gamepad you wish to use to select it. The macro will then start playing 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
