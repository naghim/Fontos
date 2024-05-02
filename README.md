# Fontos: Font Finder and Collector

This application allows you to check whether the fonts in an .ass subtitle are installed on your system or not, as well as collect the fonts into a directory.

It will tell you which fonts are missing. Correct each font and try again.

If no fonts are missing, the fonts will be collected into a directory called `fonts`.

# Usage

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
