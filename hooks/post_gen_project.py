#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
ROOT_DIR_PATTERN = '$((ROOTDIR))'


if __name__ == '__main__':
    for root, dirs, files in os.walk(PROJECT_DIRECTORY):
        for filename in files:
            fullpath = os.path.join(root, filename)

            content = None

            for encoding in ('utf-8', 'latin-1'):
                try:
                    with open(os.path.join(root, filename), 'r', encoding=encoding) as fh:
                        content = fh.read()
                except UnicodeDecodeError:
                    pass

            if content is None or ROOT_DIR_PATTERN not in content:
                continue

            with open(fullpath, 'w', encoding=encoding) as fh:
                fh.write(content.replace(ROOT_DIR_PATTERN, PROJECT_DIRECTORY))

help = """
                          Jgy__
                            jWW  `""9Wf
                          _#WWW     IW
                         jWWWWW     IW
                 __,yyyyyWWWWW     IWyyyy___
            _jyWWP"^``"`.C"9*,J _.mqD:^^"WWWWWWQg__
          jgW"^.C/"    .C'     I    `D.     'D._"WQg_
        jWP` .C"       C'      I     `D._     `D._ "Qg_
      jQP`  .C    ,d^^b._      I      _.d^^b.   `D._ "Qg
     jQ^  .C"   /`   .+" \     I     / "+.   `\   `D.  XQ
    jQ'  .C'   |`  ."    )    _I    (     ".  |    `D.  4#
    Qf  .C     (   (    /    / /\    \     )  )     `D.  Qg
   jW   C'      \__\_.+'    / /  \    `+._/__/       `D  jQ
   Qf   C         C        /_/    \         D         D   Qk
   Qf   C      _  C        \_\____/         D  _      D   QF
   QL   C      \`+.__     _______     ______.+'/      D   QF
   B&   C.      \   \|    ||     |    ||      /       D   Qf
   jQ   `C.      \   |____|/     |____|/__   /      .D'   jW
    TQ   `C.      \._   `+.__________/___/|_/      .D'   jQ`
     9Q   `C.      C.`+._           |   |/.D'     .D'   jQ'
      "Qg  `C.     `C.   `"+-------'   ' .D'     .D'   pW`
       ^WQy `C.     `C.        I        .D'    _.D' yW"
         ^9Qy_`C.    `C.       I       .D'   _.D jgW"
            `9WQgC.__ `C.      I      .D'  _.Dp@@"`
           ilmk `""9WQQggyyyyyygyyyyyQggQWQH""
    
Don't forget to sync to GitHub. Have fun!
"""
print(help)
