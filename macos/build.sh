#!/bin/sh
pyinstaller -y --clean gadget.spec
cp dist/gadget ~/bin
# scp dist/gadget kimird.com:/opt/kymoz/macosx
