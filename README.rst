====================
sphinxcontrib-budoux
====================

Overview
========

This is Sphinx extension to break line of heading texts by BudouX.

Simple example
--------------

From source is:

.. code-block:: rst

   あなたに寄り添う最先端のテクノロジー
   ====================================

Output without this is:

.. code-block:: html

   <h1>あなたに寄り添う最先端のテクノロジー</h1>

Output with this is:

.. code-block:: html

   <h1 style="word-break: keep-all; overflow-wrap: break-word;">あなたに<wbr/>寄り添う<wbr/>最先端の<wbr/>テクノロジー</h1>

Installation
============

.. code-block:: console

   pip install sphinxcontrib-budoux

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

Note
====

Main targets for edit are heading text, not but contents of paragraph.

If you set ``p``, ``li`` and others into `budoux_targets``, this may not work correctly that you think.

Example
=======

See `doc <https://attakei-lab.github.io/sphinxcontrib-budoux/>`__ (written by Japanese).
