# -*- coding: utf-8 -*-
"""
Created on Sun May 28 22:26:01 2023

@author: lang
"""

import numpy as np
path = './dump_match_pairs/scene0711_00_frame-001680_scene0711_00_frame-001995_matches.npz'
npz = np.load(path)
npz.files
npz['keypoints0'].shape
npz['keypoints1'].shape
npz['matches'].shape
np.sum(npz['matches']>-1)
npz['match_confidence'].shape
