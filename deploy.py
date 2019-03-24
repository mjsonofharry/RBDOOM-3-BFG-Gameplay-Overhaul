import json
import os
import sys
import zipfile

import utils

def main():
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
        mod_name = mod.game_name + '-Gameplay-Overhaul'
        target = os.path.join(project_path, 'packages',
            mod_name + ('.pk4' if mod.is_pk4 else '.zip'))
        if os.path.isfile(target):
            os.remove(target)
        print('Generating archive at', target)
        z = zipfile.ZipFile(target, 'w')
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
                z.write(src, arcname=arc)
        print('Finished packaging for', mod.game_name)
        print('')

if __name__ == '__main__':
    main()