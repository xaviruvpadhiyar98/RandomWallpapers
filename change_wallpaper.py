#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 16:45:07 2020

@author: pi
"""

from os import getcwd,listdir,system
from random import choice

wallpapers = listdir()
wallpapers.remove('change_wallpaper.py')
wallpapers.remove('download_wallpaper.py')
system(f"pcmanfm -w {getcwd()}/{choice(wallpapers)}")

