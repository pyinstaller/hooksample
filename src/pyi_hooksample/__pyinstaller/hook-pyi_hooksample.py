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
# *************************************************************************
# |docname| - A hook for the :doc:`pyi_hooksample <../__init__.py>` library
# *************************************************************************

# This is a PyInstaller `hook
# <https://pyinstaller.readthedocs.io/en/stable/hooks.html>`_.
# needed to successfully freeze
# the :doc:`pyi_hooksample package <../__init__.py>`.
# See the `PyInstaller manual <https://pyinstaller.readthedocs.io/>`_
# for more information.
#
from PyInstaller.utils.hooks import collect_data_files

# Hook global variables
# =====================
#
# For the package ``pyi_hooksample`` to be frozen successfully,
# the module ``pyi_hooksample._hidden`` needs to be frozen, too,
# as well as all data-files.
# This hook takes care about this.
# For more information see
# `hook global variables
# <https://pyinstaller.readthedocs.io/en/stable/hooks.html#hook-global-variables>`_
# in the manual for more information.

hiddenimports = ["pyi_hooksample._hidden"]
# The ``excludes`` parameter of `collect_data_files
# <https://pyinstaller.readthedocs.io/en/stable/hooks.html#useful-items-in-pyinstaller-utils-hooks>`_
# excludes ``rthooks.dat`` from the frozen executable, which is only needed when
# freezeing, but not when executing the frozen program.
datas = collect_data_files('pyi_hooksample', excludes=['__pyinstaller'])
