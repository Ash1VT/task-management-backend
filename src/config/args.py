from argparse import ArgumentParser

__all__ = [
    'parser'
]

parser = ArgumentParser()
parser.add_argument("--settings", help="Settings which should be used for app",
                    choices=['dev', 'test', 'prod'],
                    required=False,
                    default='dev',
                    type=str)
