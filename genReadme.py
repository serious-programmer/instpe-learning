import os

allFile = []


def iterate(curDir):
    dirs = os.listdir(curDir)
    # print(dirs)
    for dir in dirs:
        fullPath = os.path.join(curDir, dir)
        if dir.endswith('.md') and dir != 'README.md':
            allFile.extend(getUsefulContent(fullPath, os.path.basename(curDir)))
            # print(dir)
        elif os.path.isdir(fullPath):
            iterate(fullPath)


def getUsefulContent(file, proj):
    # print('proj ' + proj)
    contents = open(file).readlines()
    contents.reverse()
    buf = ['#' + proj + '\n']  # project name

    for line in contents:
        if line.startswith('##'):
            break
        buf.insert(1, line)

    buf.extend(['\n', '\n', "---", '\n'])  # add blank line
    return buf
    # print(contents)
    # allFile.extend(buf)
    # print(buf)
    # print(allFile)


def genFile():
    with open('README.md', 'w') as file:
        file.writelines(allFile)


iterate('./')
genFile()
print("succeed")
