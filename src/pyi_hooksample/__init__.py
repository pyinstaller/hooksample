# .. Copyright © 2020 PyInstaller Development Team
#
#   This file is part of PyInstaller Hook Sample.
#
#   PyInstaller Hook Sample is free software; you can redistribute it and/or
#   modify it under the terms of the GNU General Public License as published
#   by the Free Software Foundation; either version 3 of the License, or (at
#   your option) any later version.
#
#   PyInstaller Hook Sample is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
#   Public License for more details.
#
#   You should have received a copy of the GNU General Public License along
#   with PyInstaller Hook Sample. If not, see <http://www.gnu.org/licenses/>.
#
#   SPDX-License-Identifier: GPL-3.0-or-later
#
# ****************************************************
# ``pyi_hooksample/`` |docname| - Hook sample package
# ****************************************************
#
# This is a trivial package, which contains a hidden import and
# depends on a data file. For these reasons, this library needs
# :doc:`PyInstaller hooks <__pyinstaller/__init__.py>` in order to be
# frozen properly by PyInstaller.

import pkgutil
import importlib

__version__ = "0.1"
__all__ = ["do_import", "print_message"]

# .. _do_import:
#
# do_import
# ---------
#
# Uses ``importlib`` to import the :doc:`_hidden.py` module. Since
# PyInstaller only performs static analysis, it cannot detect this
# import.
def do_import():
     # Direct use of ``__import__()`` is discouraged in favor of
     # ``importlib.import_module()``.
    importlib.import_module('._hidden', __name__)

# .. _print_message:
#
# print_message
# -------------
#
# Relies on a data file to work correctly. PyInstaller must be
# instructed to include this file when freezing for the program to run
# correctly.
def print_message():
    msg = pkgutil.get_data(__name__, 'message.txt').decode().rstrip()
    print("Message from ", __name__, ": ", msg, sep="")
