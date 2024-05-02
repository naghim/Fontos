import shutil
import os

def install_fonts(font_folder, subtitle_fonts, installed_fonts):
    # Create the folder if it does not exist
    if not os.path.exists(font_folder):
        os.makedirs(font_folder)

    # Make sure not to install fonts twice
    fonts_installed = set()

    for font in subtitle_fonts:
        installed_ttf = installed_fonts[font]

        if installed_ttf in fonts_installed:
            # This font was already installed
            continue

        extension = os.path.splitext(installed_ttf)[-1]
        font_file = os.path.join(font_folder, f'{font}{extension}')

        if os.path.exists(font_file):
            # This font already exists in the folder
            continue

        # Copy the font into the folder
        shutil.copyfile(installed_ttf, font_file)
        fonts_installed.add(installed_ttf)