# Andy Torres
# University of Central Florida
# Department of Mechanical and Aerospace Engineering
# Last Changed: 12-14-23

# ========================
# PyRPOD: test/test_case_13.py
# ========================
# Test case for converting STL data to VTK data.
# This is accomplished by checking for the proper data format of VTK files.

import test_header
import unittest, os, sys
from pyrpod import Vehicle
from pyrpod import RPOD

class STLtoVTKChecks(unittest.TestCase):
    def test_delta_m_plots(self):

        # Path to directory holding data assets and results for a specific RPOD study.
        case_dir = '../case/stl_to_vtk/'

        # Load configuration data for RPOD analysis.
        rpod = RPOD.RPOD(case_dir)

        # Use Vehicle Object to read STL surface data.
        v = Vehicle.Vehicle()
        v.set_stl(case_dir + 'stl/' +rpod.config['stl']['vv'])

        # Convert to VTK and save in case directory.
        v.convert_stl_to_vtk(case_dir + 'results/')

if __name__ == '__main__':
    unittest.main()