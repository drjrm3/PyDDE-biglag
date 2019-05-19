"""
PyDDE -- A Python port of the C DDE solver, Solv95.

Original C code:  Simon Wood <s.wood@bath.ac.uk>
Python/C port:    Benjamin Cairns <ben.cairns@ceu.ox.ac.uk>
Cleanup:          Henning Dickten <hdickten@uni-bonn.de>
Lag change:       J. Robert Michael <jrobert.michael@gmail.com>
Last updated:     19 May 2019

This module primarily provides the class pydde.dde.

The class pydde.dde has the following methods:

  <instance>.initsolver   -- sets the tuple <instance>.SOLVER
  <instance>.initproblem  -- sets the tuple <instance>.PROB
  <instance>.solve        -- solves the delay differential equation.
  <instance>.dde          -- does all of the above in one

In addition the module provides the functions:

  pydde.pastvalue    -- for accessing the history of the integration
  pydde.pastgradient -- for accessing the history of the derivative

After solving the DDE with <instance>.solve() the user may be interested in:

  <instance>.data -- contains the times (first column) and state variablesA

"""
try:
    from .pydde import dde
    from .pydde import pastvalue
    from .pydde import pastgradient

    __all__ = ['dde', 'pastvalue', 'pastgradient']
except ImportError:
    print("Init failed!")
