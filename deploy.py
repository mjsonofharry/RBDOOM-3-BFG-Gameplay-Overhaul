import json
import os
import shutil
import sys
import zipfile
import warnings

import utils

def create_mod_package(project_path, mod, source_data, install_pk4=False):
    mod_name = mod.game_name + '_Gameplay_Overhaul'
    target = os.path.join(project_path, 'packages',
        mod_name + ('.pk4' if mod.is_pk4 else '.zip'))
    if os.path.isfile(target):
        os.remove(target)
    print('Generating archive at', target)
    z = zipfile.ZipFile(target, 'w')
    n = 0
    for source_root, source_paths in source_data:
        archive_paths = [
            (x, os.path.relpath(x, source_root))
            for x in source_paths
        ] if mod.is_pk4 else [
            (x, os.path.join(mod_name, os.path.relpath(x, source_root)))
            for x in source_paths
        ]
        print('Found', len(archive_paths),'files in', source_root)
        for src, arc in archive_paths:
            try:
                z.write(src, arcname=arc)
                print(' - {}:'.format(source_root), arc)
            except UserWarning:
                print(' - {}:'.format(source_root), arc, '- DUPLICATE')
            n += 1
    print('Zipped', n, 'files')
    print('Finished packaging for', mod.game_name)
    z.close()
    if install_pk4:
        secondary_target_dir = os.path.join(mod.game_path, mod_name)
        if not os.path.isdir(secondary_target_dir):
            os.mkdir(secondary_target_dir)
        secondary_target = os.path.join(secondary_target_dir, mod_name + '.pk4')
        if os.path.isfile(secondary_target):
            os.remove(secondary_target)
        shutil.copy(target, secondary_target)
        print('Installed package to', secondary_target)
    print('')

def main():
    warnings.filterwarnings('error')
    project_path = sys.path[0]
    print('Project root:', project_path)
    print('Reading configuration for mod definitions')
    mod_definitions = json.loads(open(utils.MOD_DEFINITION_PATH, 'r').read(),
        object_hook=utils.mod_definition_decoder)
    for mod in mod_definitions:
        print('Packaging mod for', mod.game_name)
        print('Using sources:', ', '.join(mod.data_sources))
        source_data = [
            (data_source, utils.get_source_paths(data_source,
                os.walk(data_source)))
            for data_source in mod.data_sources
        ]
        create_mod_package(project_path, mod, source_data)

if __name__ == '__main__':
    main()