import unittest
import os
import data_reduction_scripts.FullDataReduction as dr
from mantid.simpleapi import *
import numpy as np


class LokiSANSTestReduction(unittest.TestCase):
    resX = [0.00832919, 0.00899552, 0.00971516, 0.01049238, 0.01133177, 0.01223831,
            0.01321737, 0.01427476, 0.01541674, 0.01665008, 0.01798209, 0.01942065,
            0.02097431, 0.02265225, 0.02446443, 0.02642159, 0.02853531, 0.03081814,
            0.03328359, 0.03594628, 0.03882198, 0.04192774, 0.04528196, 0.04890451,
            0.05281687, 0.05704222, 0.0616056, 0.06653405, 0.07185677, 0.07760532,
            0.08381374, 0.09051884, 0.09776035, 0.10558117, 0.11402767, 0.12314988,
            0.13300187, 0.14364202, 0.15513338, 0.16754405, 0.18094758, 0.19542339,
            0.21105726, 0.22794184, 0.24617718, 0.26587136, 0.28714107, 0.31011235,
            0.33492134, 0.36171505, 0.39065225, 0.42190443, 0.45565679, 0.49210933,
            0.53147808, 0.57399632]
    resY = [1.60860275, 1.63601239, 1.62145137, 1.66173829, 1.64047339, 1.65254645,
            1.66337438, 1.68043315, 1.66881372, 1.66679861, 1.63029128, 1.59500513,
            1.54059872, 1.49554892, 1.43673333, 1.36759715, 1.29054972, 1.20856472,
            1.12530477, 1.02933663, 0.93972498, 0.85087943, 0.76595811, 0.68704794,
            0.61261893, 0.54538829, 0.48175309, 0.42634578, 0.37310166, 0.32987492,
            0.28974705, 0.25399861, 0.22421849, 0.19594944, 0.17339531, 0.15199601,
            0.13282122, 0.11642094, 0.10348805, 0.09155015, 0.08166887, 0.07362112,
            0.06600545, 0.06128553, 0.05427474, 0.04819955, 0.0445715, 0.04047412,
            0.0364507, 0.03395268, 0.03174567, 0.02838911, 0.02594106, 0.02509733,
            0.02411883]

    def test_run_script(self):
        folder = os.path.dirname(__file__)
        folder += "/test_data/"
        directBeamFile = 'DirectBeam_20feb_full_v3.dat'
        moderatorFile = 'ModeratorStdDev_TS2_SANS_LETexptl_07Aug2015.txt'
        lokiReduction = dr.LokiSANSTestReduction(49338, 49339, 49334, 49335, 49335, folder, directBeamFile,
                                                 moderatorFile)
        lokiReduction.execute()

        resultWs = mtd['reduced']
        x = resultWs.extractX()
        y = resultWs.extractY()

        self.assertTrue(np.allclose(x[0], self.resX))
        self.assertTrue(np.allclose(y[0], self.resY))


if __name__ == '__main__':
    unittest.main()
