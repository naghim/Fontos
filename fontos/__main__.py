from colorama import Fore, Style
from fontos import windows, font, subtitle, install
import sys
import os

def main():
    font_folder = 'fonts'
    subtitle_filename = sys.argv[1] if len(sys.argv) > 1 else 'subtitle.ass'

    if not os.path.exists(subtitle_filename):
        print(f'{subtitle_filename} is missing!')
        sys.exit()

    # First, find all installed fonts...
    installed_font_ttfs = windows.find_installed_ttfs()

    # Second, find the font names of all installed fonts...
    installed_fonts = {}
    font.parse_font_names(installed_font_ttfs, installed_fonts)

    # Third, find the fonts in the subtitle...
    subtitle_fonts = subtitle.find_fonts_in_subtitle(subtitle_filename)

    # Finally, let's see if all fonts are installed.
    all_installed = True

    for subtitle_font in subtitle_fonts:
        if subtitle_font in installed_fonts:
            print(subtitle_font, Fore.GREEN + 'INSTALLED', Style.RESET_ALL)
        else:
            all_installed = False

    if all_installed:
        # All fonts are installed, let's save the fonts into a separate folder!
        install.install_fonts(font_folder, subtitle_fonts, installed_fonts)
        print('Installed fonts to', os.path.abspath(font_folder))
        return
    
    # Not all fonts are found, let's print the ones that are missing
    for subtitle_font in subtitle_fonts:
        if subtitle_font not in installed_fonts:
            print(subtitle_font, Fore.RED + 'NOT INSTALLED', Style.RESET_ALL)

    input()

if __name__ == '__main__':
    main()
