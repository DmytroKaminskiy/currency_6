import sys

from meta import meta
from engine import engine

command = sys.argv[1]

if command == 'create':
    meta.create_all(engine)
