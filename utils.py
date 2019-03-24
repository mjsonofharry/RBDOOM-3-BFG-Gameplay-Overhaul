import collections
import os

MOD_DEFINITION_PATH = 'mods.json'

Mod = collections.namedtuple('Mod', ['game_name', 'is_pk4', 'data_sources', 'game_path'])

def get_source_paths(source_root, source_walk):
    return [
        os.path.join(r, f)
        for r,d,fs in source_walk for f in fs
        if fs and not d
    ]

def mod_definition_decoder(obj):
    return Mod(game_name=obj['game_name'], is_pk4=obj['is_pk4'],
        data_sources=obj['data_sources'], game_path=obj['game_path'])
