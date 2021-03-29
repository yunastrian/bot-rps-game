import getopt
import sys
from typing import Dict
import yaml

moves_lang2en: Dict = dict()
moves_en2lang: Dict = dict()

# default value
variables_filename = 'variables.yml'
lang = 'en'

variables_file = open(variables_filename, 'r')
variable_dict: Dict = yaml.safe_load(variables_file)
variables_file.close()

supported_languages = variable_dict.keys()

argv = sys.argv[1:]
usage_message = (f"Usage: python {__file__} [OPTIONS]\n"
                 "\n"
                 "Options:\n"
                 "-l, --language     Select the language of the game.\n"
                 "                   The default is english.\n")

try:
    opts, args = getopt.getopt(argv, "hl:",
                               ["help", "language ="])
except Exception:
    print('Invalid option\n')
    print(usage_message)
    sys.exit(2)

for opt, arg in opts:
    if opt in ("-h", "--help"):
        print(usage_message)
        sys.exit()
    elif opt in ("-l", "--language"):
        if arg not in supported_languages:
            print(f"Invalid arguments for language: {arg}")
            print(f'Supported languages: {", ".join(supported_languages)}')
            sys.exit(3)
        lang = arg

variables: Dict = variable_dict[lang]

for en, lang in variables['moves'].items():
    moves_en2lang[en] = lang
    moves_lang2en[lang] = en

player_move = ''
while player_move not in moves_lang2en:
    input_message = variables['messages']['input'] \
        .format(moves=", ".join(moves_lang2en.keys()))
    player_move = input(input_message).lower().strip()

player_move = moves_lang2en[player_move]
bot_move = 'rock'
if (player_move == 'paper'):
    bot_move = 'scissor'
elif (player_move == 'rock'):
    bot_move = 'paper'
bot_move = moves_en2lang[bot_move]

print()
print(variables['messages']['bot_pick'].format(bot_move=bot_move))
print(variables['messages']['defeat'])
