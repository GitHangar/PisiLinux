#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("configure.ac", "-pedantic ", "")
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --with-emf \
                         --with-swf")
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.doman("doc/pstoedit.1")
    pisitools.dohtml("doc/*.htm")

    pisitools.dodoc("doc/readme.txt")
