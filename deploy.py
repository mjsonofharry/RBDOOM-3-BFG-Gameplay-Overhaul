import os
import sys
import zipfile

MOD_NAME = 'RBDOOM-3-BFG-Gameplay-Overhaul'
OUTPUT_NAME = 'RBDOOM-3-BFG-Gameplay-Overhaul.zip'
EXCLUSIONS = [
    OUTPUT_NAME,
    '.git',
    '.vscode',
    '.gitignore',
    'generated',
    'screenshots',
    'deploy.py',
    'README.md',
    '.cm'
]

def traverse(root):
    successors = [
        os.path.join(root, x) for x in os.listdir(root)
        if not any([x.endswith(e) for e in EXCLUSIONS])
    ]
    files = [x for x in successors if os.path.isfile(x)]
    directories = [x for x in successors if os.path.isdir(x)]
    traversals = [traverse(os.path.join(root, x)) for x in directories]
    for x in traversals:
        files = files + x
    return files

def main():
    project_path = sys.path[0]
    print('Project root:', project_path)

    print('Finding project files...')
    files = traverse(project_path)
    print('Found the following project files')
    [print(' -', x) for x in files]
    
    target = os.path.join(project_path, OUTPUT_NAME)
    with zipfile.ZipFile(target, 'w') as zip:
        print('Generating archive')
        [zip.write(x, arcname=os.path.join(MOD_NAME,
            os.path.relpath(x, project_path))) for x in files]
        print('Wrote:', target)

if __name__ == '__main__':
    main()