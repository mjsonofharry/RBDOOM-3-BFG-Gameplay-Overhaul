import hashlib
import json
import os
import shutil
import sys

import utils

def main():
    project_path = sys.path[0]
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