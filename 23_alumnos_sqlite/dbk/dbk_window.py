# Copyright          2022 DBK. All rights reserved.       ####   ####   #   #
# Author: Davide P. Fragnito <davidepie90@gmail.com>      #   #  #   #  #  #
#                                                         #   #  ####   ###
# Python API (main graphics display)                      #   #  #   #  #  #
#	                                                      ####   ####   #   #

from abc import ABC, abstractmethod

class DBK_Window(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def icon(self, icon):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def __del__(self):
        pass