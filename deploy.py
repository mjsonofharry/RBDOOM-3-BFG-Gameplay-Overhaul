import collections
import os
import shutil
import sys
import zipfile

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

def traverse(root):
    successors = [
        os.path.join(root, x) for x in os.listdir(root)
        if not any([x.endswith(e) for e in EXCLUSIONS])
    ]
    files = [x for x in successors if os.path.isfile(x)]
    directories = [x for x in successors if os.path.isdir(x)]
    for x in [traverse(os.path.join(root, x)) for x in directories]:
        files = files + x
    return files

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
        target = os.path.join(project_path, mod_name + '.pk4') if mod.is_pk4 else os.path.join(project_path, mod_name + '.zip')
        if os.path.isfile(target):
            os.remove(target)
        with zipfile.ZipFile(target, 'w') as zip:
            print('Generating archive...')
            for source_root, source_paths in source_data:
                archive_paths = [
                    (x, os.path.relpath(x, source_root))
                    for x in source_paths
                ] if mod.is_pk4 else [
                    (x, os.path.join(mod_name, os.path.relpath(x, source_root)))
                    for x in source_paths
                ]
                print('Found the following files in', source_root)
                [print(' -', x) for x,y in archive_paths]
                for src, arc in archive_paths:
                    zip.write(src, arcname=arc)
        print('Finished packaging for', mod.game_name)
        print('')

if __name__ == '__main__':
    main()