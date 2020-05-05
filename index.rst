*************************************
PyInstaller hook sample documentation
*************************************

This package demonstrates defining a library which includes
PyInstaller hooks along with tests for those hooks. It is intended to
provide a guide for integrating PyInstaller hooks and tests into a
package. All source is `available on Github
<https://github.com/pyinstaller/hooksample>`_. A brief walkthrough:

* This package provides the ``pyi_hooksample`` library, implemented in
  :doc:`src/pyi_hooksample/__init__.py`, which defines two functions:

    * :ref:`do_import`, which uses ``importlib`` to import the
      :doc:`src/pyi_hooksample/_hidden.py` module. Since PyInstaller only
      performs static analysis, it cannot detect this import.

    * :ref:`print_message`, which relies on a data file to work correctly.
      PyInstaller must be instructed to include this file when
      freezing for the program to run correctly.

* Therefore, this package also provides a :doc:`hook
  <src/pyi_hooksample/__pyinstaller/hook-pyi_hooksample.py>` to
  fix these two problems. It also :ref:`registers this hook with
  PyInstaller <hook_registration>`, so that all PyInstaller builds
  will have this hook available if needed.

* Finally, it provides a short :doc:`test script
  <src/pyi_hooksample/__pyinstaller/test_hooksample_packaging.py>`
  to ensure the hooks work correctly. This is also :ref:`registered with
  PyInstaller <tests_registration>`, which enables running this test
  in two locations:

  * This package can run tests to ensure the hook produces a working
    executable when frozen by PyInstaller. For example, :ref:`CI
    testing via Travis <run_pyi_tests>` invokes these tests.

  * PyInstaller can also run this test during its development process,
    ensuring that any updates to PyInstaller don't break this
    package's freeze process. After integrating this approach in your
    library, `post an issue
    <https://github.com/pyinstaller/pyinstaller/issues>`_ so the
    PyInstaller team can add your package to the list of packages
    covered by CI.


Contents
========
.. toctree::
    :maxdepth: 1

    src/pyi_hooksample/__init__.py
    src/pyi_hooksample/__pyinstaller/__init__.py
    tests/test_basic.py
    setup.cfg
    .travis.yml


Installation
============
From a terminal/command prompt:

#. Upgrade pip::

       python -m pip install -U pip

#. Install this package with the optional ``test`` and ``docs``
   requirements::

       pip install -e .[test,docs]

#. Run the tests; see also :ref:`notes <run_pyi_tests>` on this::

       python -m PyInstaller.utils.run_tests --include_only pyi_hooksample.

#. Build the docs::

       sphinx-build -d _build/doctrees . _build


License
=======

Copyright © 2020 PyInstaller Development Team

This file is part of PyInstaller Hook Sample.

PyInstaller Hook Sample is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or (at your
option) any later version.

PyInstaller Hook Sample is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
details.

You should have received a copy of the GNU General Public License along with
PyInstaller Hook Sample. If not, see <http://www.gnu.org/licenses/>.

SPDX-License-Identifier: GPL-3.0-or-later
