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
# ********************************************************
# |docname| - Test freezing this project using PyInstaller
# ********************************************************
#
# This file's name begins with ``test_``, which means it will be
# automatically `discovered by pytest
# <https://docs.pytest.org/en/latest/goodpractices.html#test-discovery>`_.
#
import subprocess

from PyInstaller import __main__ as pyi_main
#
# Tests
# =====
#
# Test out the package by importing it, then running functions from it.
#
def test_pyi_hooksample(tmp_path):
    workpath = tmp_path / "build"
    distpath = tmp_path / "dist"
    app = tmp_path / "userapp.py"
    app.write_text("\n".join([
        "import pyi_hooksample",
        "pyi_hooksample.do_import()",
        "pyi_hooksample.print_message()"]))
    args = [
        # use options to get all generated file in tmp_path
        '--workpath', str(workpath),
        '--distpath', str(distpath),
        '--specpath', str(tmp_path),
        str(app),
        ]
    pyi_main.run(args)
    subprocess.run([str(distpath / "userapp" / "userapp")], check=True)
