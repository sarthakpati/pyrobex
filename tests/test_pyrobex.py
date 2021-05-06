#!/usr/bin/env python
"""Tests for `pyrobex` package."""

from pathlib import Path
import os

import nibabel as nib
import pytest

from pyrobex.pyrobex import robex, _find_assets


@pytest.fixture
def test_image():
    assets = Path(_find_assets())
    test_file = assets / "ROBEX" / "ref_vols" / "atlas.nii.gz"
    return nib.load(test_file)


@pytest.mark.skipif(os.name == 'posix', reason="Mac OS X not currently supported.")
def test_content(test_image):
    stripped, mask = robex(test_image)
    stripped_shape = stripped.get_fdata().shape
    mask_shape = mask.get_fdata().shape
    image_shape = test_image.get_fdata().shape
    assert stripped_shape == mask_shape
    assert mask_shape == image_shape
