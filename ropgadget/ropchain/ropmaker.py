#!/usr/bin/env python2
## -*- coding: utf-8 -*-
##
##  Jonathan Salwan - 2014-05-13
## 
##  http://shell-storm.org
##  http://twitter.com/JonathanSalwan
## 
##  This program is free software: you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software  Foundation, either  version 3 of  the License, or
##  (at your option) any later version.
##

from capstone           import *
from arch.ropmakerx86   import *
from arch.ropmakerx64   import *
from arch.ropmakerx86_rawelf import *
from arch.ropmakerx64_rawelf import *

class ROPMaker:
    def __init__(self, binary, gadgets, offset):
        self.__binary  = binary
        self.__gadgets = gadgets
        self.__offset  = offset

        self.__handlerArch()

    def __handlerArch(self):
        print self.__binary.getArch(), CS_ARCH_X86 
        print self.__binary.getArchMode(), CS_MODE_32
        print self.__binary.getFormat()
        if self.__binary.getArch() == CS_ARCH_X86           \
            and self.__binary.getArchMode() == CS_MODE_32   \
            and self.__binary.getFormat() == "ELF":
            ROPMakerX86(self.__binary, self.__gadgets, self.__offset)

        elif self.__binary.getArch() == CS_ARCH_X86         \
            and self.__binary.getArchMode() == CS_MODE_64   \
            and self.__binary.getFormat() == "ELF":
            ROPMakerX64(self.__binary, self.__gadgets, self.__offset)

        elif self.__binary.getArch() == CS_ARCH_X86           \
            and self.__binary.getArchMode() == CS_MODE_32   \
            and self.__binary.getFormat() == "Raw":
            print "\n[-] ROPMaker - Is a raw binary. Use ELF format searching by default."
            ROPMakerX86_rawelf(self.__binary, self.__gadgets, self.__offset)

        elif self.__binary.getArch() == CS_ARCH_X86         \
            and self.__binary.getArchMode() == CS_MODE_64   \
            and self.__binary.getFormat() == "Raw":
            print "\n[-] ROPMaker - Is a raw binary. Use ELF format searching by default."
            ROPMakerX64_rawelf(self.__binary, self.__gadgets, self.__offset)

        else:
            print "\n[Error] ROPMaker.__handlerArch - Arch not supported yet for the rop chain generation"

