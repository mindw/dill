#!/usr/bin/env python
#
# Author: Mike McKerns (mmckerns @caltech and @uqfoundation)
# Copyright (c) 2008-2015 California Institute of Technology.
# License: 3-clause BSD.  The full license text is available at:
#  - http://trac.mystic.cacr.caltech.edu/project/pathos/browser/dill/LICENSE

def main():
    import sys
    from . import load
    for file in sys.argv[1:]:
        print load(open(file,'r'))

if __name__ == '__main__':
    main()
