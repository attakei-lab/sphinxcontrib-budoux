====================
sphinxcontrib-budoux
====================

.. note:: This is experimental library.

Overview
========

This is Sphinx extension to break line of heading texts by BudouX.

Installation
============

.. code-block:: console

   pip install --find-links=https://github.com/attakei-lab/sphinxcontrib-budoux/releases sphinxcontrib-budoux

Usage
=====

.. code-block:: python

   extensions = [
       "sphinxcontrib.budoux",
   ]
   
   # Tag to ijnect for splitted texts
   budoux_split_tag = "wbr"
   # Style for splitted-tag
   budoux_split_style = "budoux_split_style", "word-break: keep-all; overflow-wrap: break-word;"
   # Target tags for apply BudouX
   budoux_targets = ["h1", "h2"]

Example
=======

See `doc <doc/>`_ (written by Japanese).
