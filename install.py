import hashlib
import json
import os
import shutil
import sys

import utils
import deploy

def install_bfg_mod(mod, source_data, clean_install=False):
    mod_name = mod.game_name + '_Gameplay_Overhaul'
    mod_install_root = os.path.join(mod.game_path, mod_name)
    if clean_install:
        print('Cleaning previous installations at', mod_install_root)
        if os.path.isdir(mod_install_root):
            shutil.rmtree(mod_install_root)
    n = 0
    for source_root, source_paths in source_data:
        copy_paths = [
            (x, os.path.join(
                mod.game_path,
                mod_name,
                os.path.relpath(x, source_root)))
            for x in source_paths
        ]
        print('Found', len(copy_paths),'files in', source_root)
        for src, dst in copy_paths:
            dst_dir = os.path.dirname(dst)
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)
            if os.path.isfile(dst):
                with open(src, 'rb') as f_src, open(dst, 'rb') as f_dst:
                    left = hashlib.md5(f_src.read()).hexdigest()
                    right = hashlib.md5(f_dst.read()).hexdigest()
                    if left == right:
                        continue
                os.remove(dst)
            shutil.copy(src, dst)
            print(' - Wrote:', dst)
            n += 1
        print('Copied', n, 'files')
        print('Finished installing for', mod.game_name)
        print('')

def main():
    project_path = sys.path[0]
    args = sys.argv[1:] if len(sys.argv) > 1 else []
    print('Project root:', project_path)
    print('Reading configuration for mod definitions')
    mod_definitions = json.loads(open(utils.MOD_DEFINITION_PATH, 'r').read(),
        object_hook=utils.mod_definition_decoder)
    for mod in mod_definitions:
        if not mod.game_path:
            print('No install path found for', mod.game_name, '- Skipping')
            continue
        print('Installing mod for', mod.game_name)
        print('Using sources:', ', '.join(mod.data_sources))
        source_data = [
            (data_source, utils.get_source_paths(data_source,
                os.walk(data_source)))
            for data_source in mod.data_sources
        ]
        if mod.is_pk4:
            deploy.create_mod_package(project_path, mod, source_data, install_pk4=True)
        else:
            install_bfg_mod(mod, source_data, '--clean' in args)

if __name__ == '__main__':
    main()