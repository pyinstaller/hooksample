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
# *******************************************************
# |docname| - A run-time hook for the hook sample library
# *******************************************************
#
# If some module needs extra set-up at run-time
# (e.g. setting an environment variable)
# this can be done in a *run-time hook*.
# The same *run-time hook* script might be used for several module,
# but of course sould only be run once.
# This is why *run-time hooks* are to be listed in the
# :doc:`rthooks.dat <../rthooks.dat>` file.
#
# Thus dummy run-time hook does nothing useful,
# just shows that it was included.
print(">>> Hook sample run-time hook was executed. <<<")
