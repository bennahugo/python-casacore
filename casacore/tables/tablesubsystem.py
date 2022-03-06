# table.py: Python PlainTable functions
# Copyright (C) 2022
# South African Radio Astronomy Observatory
#
# This library is free software; you can redistribute it and/or modify it
# under the terms of the GNU Library General Public License as published by
# the Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Library General Public
# License for more details.
#
# You should have received a copy of the GNU Library General Public License
# along with this library; if not, write to the Free Software Foundation,
# Inc., 675 Massachusetts Ave, Cambridge, MA 02139, USA.
#
# Correspondence concerning AIPS++ should be addressed as follows:
#        Internet email: aips2-request@nrao.edu.
#        Postal address: AIPS++ Project Office
#                        National Radio Astronomy Observatory
#                        520 Edgemont Road
#                        Charlottesville, VA 22903-2475 USA

from ._tables import TableSubSystem
def systemAwareOfTablesProcessWide():
    """
    Switch the CC API to use a table cache over the entire
    process. This is the default behaviour of the table system,
    meaning that the process is aware of all tables open on the
    process. Only one PlainTable object per table may then
    be open at any point in time. The calling process is aware of all
    such open tables across all threads. At present the table
    system itself is not threadsafe, but this method is provided to ensure
    the traditionally assumed behaviour of the TableCache
    system. This globally-aware caching has the side-effect
    of synchronizing IO to a PlainTable (or derived object) on the process.
    When a PlainTable is reopened in e.g. update mode any existing
    table object within the process pointing to the same disk 
    location is upgraded to writable as well through this system
    WARNING :-: calling this closes all open tables across
    Has no effect if already on a cache per process mode
    the **process**.
    """
    TableSubSystem._useProcessWideTableCache()

def systemAwareOfTablesPerThread():
    """
    New: switch the CC API to use a table cache per thread.
    Each thread is treated as sole-custodian of the tables
    it creates in auto locking and is unaware of tables created
    in other threads (regardless of auto-locking mode). If autolocking
    is used it is restricted to automatically apply within the current
    thread.
    This mode requires all locks allocated to be readonly to ensure
    database consistency
    Has no effect if already on a cache per thread mode
    WARNING :-: calling this closes all open tables across
    the **process*
    """
    TableSubSystem._useTableCachePerThread()

def isSystemAwareOfTablesProcessWide():
    """
    Check if the table system is currently set to cache process wide
    See also:: PlainTable::useProcessWideTableCache() and
                PlainTable::useTableCachePerThread()
    Warning:: boolean returned may become stale while you are checking
    if running in threaded mode. It is strongly suggested that you set this
    behaviour only in the main thread
    """
    return TableSubSystem._isUsingTableCachePerProcess()