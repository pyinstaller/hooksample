#
# Copyright © 2020 PyInstaller Development Team
#
# This file is part of PyInstaller Hook Sample.
#
# PyInstaller Hook Sample is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or (at your
# option) any later version.
#
# PyInstaller Hook Sample is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
# Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# PyInstaller Hook Sample. If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

import pkgutil
import importlib

__version__ = "0.1"
__all__ = ["do_import", "print_message"]

def do_import():
     # Direct use of __import__() is also discouraged in favor of
     # importlib.import_module().
    importlib.import_module('._hidden', __name__)

def print_message():
    msg = pkgutil.get_data(__name__, 'message.txt').decode().rstrip()
    print("Message from ", __name__, ": ", msg, sep="")
