# Copyright © SixtyFPS GmbH <info@slint.dev>
# SPDX-License-Identifier: GPL-3.0-only OR LicenseRef-Slint-Royalty-free-1.1 OR LicenseRef-Slint-commercial

import pytest
from slint import load_file, CompileError
import os


def test_load_file(caplog):
    module = load_file(os.path.join(os.path.dirname(
        __spec__.origin), "test_load_file.slint"), quiet=False)

    assert "The property 'color' has been deprecated. Please use 'background' instead" in caplog.text

    assert list(module.__dict__.keys()) == ["App"]
    instance = module.App()
    del instance


def test_load_file_fail():
    with pytest.raises(CompileError, match="Could not compile non-existent.slint"):
        load_file("non-existent.slint")