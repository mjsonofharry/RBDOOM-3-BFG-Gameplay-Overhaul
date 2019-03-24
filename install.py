import collections
import hashlib
import os
import shutil
import sys

Mod = collections.namedtuple('Mod', ['game_name', 'is_pk4', 'data_sources', 'game_path'])

EXCLUSIONS = [
    '.zip',
    '.git',
    '.vscode',
    '.gitignore',
    'generated',
    'screenshots',
    'deploy.py',
    'README.md',
    '.cm'
]

MOD_DEFINITIONS = [
    Mod(
        game_name='RBDOOM-3-BFG',
        is_pk4=False,
        data_sources=['shared', 'bfg_common', 'bfg_rbdoom'],
        game_path='D:\\RBDOOM-3-BFG'
    ),
    Mod(
        game_name='Classic-RBDOOM-3-BFG',
        is_pk4=False,
        data_sources=['shared', 'bfg_common', 'bfg_classic-rbdoom'],
        game_path='D:\\Classic-RBDOOM-3-BFG'
    ),
    Mod(
        game_name='Doom-3',
        is_pk4=True,
        data_sources=['shared', 'd3_common'],
        game_path=None
    )
]

def get_source_paths(source_root, source_walk):
    return [
        os.path.join(r, f)
        for r,d,fs in source_walk for f in fs
        if fs and not d and not any([f.endswith(e) for e in EXCLUSIONS])
    ]

def main():
    project_path = sys.path[0]
    print('Project root:', project_path)
    for mod in MOD_DEFINITIONS:
        if not mod.game_path:
            print('No install path found for', mod.game_name, '- Skipping')
            continue
        print('Installing mod for', mod.game_name)
        print('Using sources:', ', '.join(mod.data_sources))
        source_data = [
            (data_source, get_source_paths(data_source, os.walk(data_source)))
            for data_source in mod.data_sources
        ]
        mod_name = mod.game_name + '-Gameplay-Overhaul'
        for source_root, source_paths in source_data:
            copy_paths = [
                (x, os.path.join(
                    mod.game_path,
                    mod_name,
                    os.path.relpath(x, source_root)))
                for x in source_paths
            ]
            print('Found the following files in', source_root)
            [print(' -', x) for x,y in copy_paths]
            print('Copying...')
            skipped = 0
            for src, dst in copy_paths:
                dst_dir = os.path.dirname(dst)
                if not os.path.exists(dst_dir):
                    os.makedirs(dst_dir)
                if os.path.isfile(dst):
                    with open(src, 'rb') as f_src, open(dst, 'rb') as f_dst:
                        left = hashlib.md5(f_src.read()).hexdigest()
                        right = hashlib.md5(f_dst.read()).hexdigest()
                        if left == right:
                            skipped += 1
                            continue
                    os.remove(dst)
                shutil.copy(src, dst)
            print('Copied', len(copy_paths) - skipped, 'files')
            print('Skipped', skipped, 'files')
        print('Finished installing for', mod.game_name)
        print('')

if __name__ == '__main__':
    main()