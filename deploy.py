import collections
import os
import sys
import zipfile

Mod = collections.namedtuple('Mod', ['name', 'is_pk4', 'data_sources'])

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
    Mod('RBDOOM-3-BFG', is_pk4=False, data_sources=['shared', 'bfg_common', 'bfg_rbdoom']),
    Mod('Classic-RBDOOM-3-BFG', is_pk4=False, data_sources=['shared', 'bfg_common', 'bfg_classic-rbdoom']),
    Mod('Doom-3', is_pk4=True, data_sources=['shared'])
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

def main():
    project_path = sys.path[0]
    print('Project root:', project_path)
    for game_name, is_pk4, mod_data_sources in MOD_DEFINITIONS:
        print('Working on:', game_name)
        print('Using sources:', mod_data_sources)
        mod_name = game_name + '-Gameplay-Overhaul'
        target = os.path.join(project_path, mod_name + '.pk4') if is_pk4 else os.path.join(project_path, mod_name + '.zip')
        with zipfile.ZipFile(target, 'w') as zip:
            print('Generating archive...')
            for data_source, data_paths in [
                (data_source, traverse(os.path.join(project_path, data_source)))
                for data_source in mod_data_sources
            ]:
                data_source_path = os.path.join(project_path, data_source)
                for path in data_paths:
                    print('Zipping:', path)
                    arcname = os.path.relpath(path, data_source) if is_pk4 else os.path.join(mod_name, os.path.relpath(path, data_source))
                    zip.write(path, arcname=arcname)
            print('Wrote:', target)
        print('')

if __name__ == '__main__':
    main()