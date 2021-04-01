.. raw:: html

   <h3 align="center">

Project generator and manager for FastAPI.

.. raw:: html

   </h3>

.. raw:: html

   <p align="center">

.. raw:: html

   </p>

--------------

**Source Code**: View it on
`Github <https://github.com/sxhxliang/fastapi-cli>`__

--------------

Features 🚀
----------

-  .. rubric:: Creates customizable **project boilerplate.**
      :name: creates-customizable-project-boilerplate.

-  .. rubric:: Creates customizable **app boilerplate.**
      :name: creates-customizable-app-boilerplate.

-  .. rubric:: Handles the project structuring for you.
      :name: handles-the-project-structuring-for-you.

-  .. rubric:: Optional Dockerfile generation.
      :name: optional-dockerfile-generation.

-  .. rubric:: Optional docker-compose generation for your project
      needs.
      :name: optional-docker-compose-generation-for-your-project-needs.

-  .. rubric:: Optional pre-commit hook generation.
      :name: optional-pre-commit-hook-generation.

Installation 📌
--------------

-  Prerequisites

   -  Python 3.6 +

Manage FastAPI can be installed by running

.. code:: python


   pip3 install git+https://github.com/sxhxliang/fastapi-cli
   # or
   git clone https://github.com/sxhxliang/fastapi-cli
   cd fastapi-cli && python3 setup.py develop

Getting started 🎈
-----------------

Easiest way to start is using the defaults:

.. code:: bash

   fastapi startproject [name]

But there is an **interactive** mode!

.. code:: bash

   fastapi startproject [name] --interactive

Command line options 🧰
----------------------

Manage FastAPI provides three different commands.

You can list them with

.. code:: bash

   fastapi --help

The idea is to have a highly customizable CLI, but at the same time a
simple interface for new users. You can see the available options for
``startproject`` running ``fastapi startproject --help``:

The other commands are already available but the current implementation
is too shallow. More details about ``startapp`` and ``run`` commands
will be provided once they have more functionalities, at the moment you
can run ``startapp`` by just:

.. code:: bash

   fastapi startapp {name}

On the other hand, the ``run`` command expects you to have a
``startproject`` structure:

.. code:: bash

   fastapi run

License
-------

This project is licensed under the terms of the MIT license.
