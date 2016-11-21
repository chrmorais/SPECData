# Author: Jasmine Oliveira
# Date: 07/01/2016
# peaks_removal:
#       Module that removes peak table entries:
#       Functions:
#                   * remove_all(conn, mid)
#                   * remove_peak(conn, pid)

from tables.entry.entry_molecules import mid_exists
from tables.entry.entry_peaks import pid_exists


def remove_all(conn, mid):
    """
    Removes all entries for a specified molecule
    :param conn: Connection to sqlite3 database
    :param mid: Molecule entry ID (mid) to remove associated peaks
    :return: True, if peaks are removed successfuly, otherwise False
    """
    if(mid_exists(conn, mid) is False):
        print "[ ERROR: Molecule entry does not exist. Cancelling action! ]"
        return False

    conn.execute("DELETE FROM peaks WHERE mid={m}".format(m=mid))
    conn.commit()

    return True


def remove_peak(conn, pid):
    """
    Removes a specified peak entry, by its pid
    :param conn: Connection to sqlite3 database
    :param pid: Peak entry ID (pid
    :return: True, if peak removes successfuly, otherwise False
    """
    # Determine if pid exists
    if(pid_exists(conn, pid) is False):
        # Peak does not exist
        print "[ ERROR: Peak entry does not exist. Cancelling action. ]"
        return False

    # Exists, remove peak
    conn.execute("DELETE FROM peaks WHERE pid={p}".format(p=pid))
    conn.commit()

    return True

