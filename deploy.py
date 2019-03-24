import collections
import os
import shutil
import sys
import zipfile

Mod = collections.namedtuple('Mod', ['name', 'is_pk4', 'data_sources', 'install_path'])

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
    Mod('RBDOOM-3-BFG', is_pk4=False, data_sources=['shared', 'bfg_common', 'bfg_rbdoom'], install_path='D:\\RBDOOM-3-BFG'),
    Mod('Classic-RBDOOM-3-BFG', is_pk4=False, data_sources=['shared', 'bfg_common', 'bfg_classic-rbdoom'], install_path='D:\\Classic-RBDOOM-3-BFG'),
    Mod('Doom-3', is_pk4=True, data_sources=['shared', 'd3_common'], install_path=None)
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
    for game_name, is_pk4, mod_data_sources, install_path in MOD_DEFINITIONS:
        print('Working on:', game_name)
        print('Using sources:', mod_data_sources)
        mod_name = game_name + '-Gameplay-Overhaul'
        target = os.path.join(project_path, mod_name + '.pk4') if is_pk4 else os.path.join(project_path, mod_name + '.zip')
        os.remove(target)
        with zipfile.ZipFile(target, 'w') as zip:
            print('Generating archive...')
            for data_source, data_paths in [
                (data_source, traverse(os.path.join(project_path, data_source)))
                for data_source in mod_data_sources
            ]:
                data_source_path = os.path.join(project_path, data_source)
                for path in data_paths:
                    print('Zipping:', path)
                    relative_path = os.path.relpath(path, data_source) if is_pk4 else os.path.join(mod_name, os.path.relpath(path, data_source))
                    zip.write(path, arcname=relative_path)
                    if install_path and not is_pk4:
                        copy_path = os.path.join(install_path, relative_path)
                        copy_dir_path = os.path.dirname(copy_path)
                        if not os.path.exists(copy_dir_path):
                            os.makedirs(copy_dir_path)
                        if os.path.isfile(copy_path):
                            os.remove(copy_path)
                        shutil.copy(path, copy_path)
            print('Wrote:', target)
        print('')

if __name__ == '__main__':
    main()