import argparse
parser = argparse.ArgumentParser(description='der parser ist fürs skript argparse_test')
parser.add_argument('file', help='eine datei muss gegeben werden')
parser.add_argument('-n', '--number', type=int, default=1, help='eine zahl ist bei bedarf anzugeben, die ist kein muss')
parser.add_argument('-q', '--quiet', action='store_true', default=False, help='das argument ist auch erst bei bedarf anzugeben')
args = parser.parse_args() 
print(args.file, args.number, args.quiet)
