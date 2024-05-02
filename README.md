# Fontos: Font Finder and Collector

This application allows you to check whether the fonts in an .ass subtitle are installed on your system or not, as well as collect the fonts into a directory.

It will tell you which fonts are missing. Correct each font and try again.

If no fonts are missing, the fonts will be collected into a directory called `fonts`.

# Usage (executable)

First, download the latest release from the repository: [GitHub Releases](https://github.com/naghim/Fontos/releases)

To use the program, drag a subtitle file into the `Fontos.exe` program.

The program will open a terminal window and will evaluate whether the fonts in the subtitle are installed or not.

If all fonts are installed, they will be collected into the `fonts` directory.

# Usage (Git repository)

First, install the Python requirements:

```bash
python -m pip install -r requirements.txt
```

Second, save the desired subtitle as `subtitle.ass`.

Third, run the Python program on Windows:

```bash
python -m fontos
```

This program is only supported on Windows at the moment.
