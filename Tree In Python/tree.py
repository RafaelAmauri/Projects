import os
from argparse import ArgumentParser


def make_parser():
    parser = ArgumentParser(description="Define the parameters")

    parser.add_argument('-d', type=str, required=False, 
                        help='The root directory where the exploration starts. If unspecified, will use ./'
                        )

    parser.add_argument('-maxdepth', type=int, required=False, 
                        help='How many directory deep the program will descend.'
                        )

    parser.set_defaults(d='./', maxdepth=-1)

    return parser


def listDir(currentDir, currentDepth=0):
    isSubDir = 1 if currentDepth != 0 else 0
    subFiles = [os.path.join(currentDir, file) for file in os.listdir(currentDir)]

    for sub in subFiles:
        print(f"❘{'――'*currentDepth}{'❘'*isSubDir} {sub.split('/')[-1]}")
            
        if os.path.isdir(sub):
            listDir(sub, currentDepth+1)


def main():
    args     = make_parser().parse_args()
    MAXDEPTH = args.maxdepth
    ROOT     = args.d

    listDir(ROOT)

if __name__ == '__main__':
    main()
