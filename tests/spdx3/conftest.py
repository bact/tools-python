# SPDX-FileCopyrightText: 2026-present SPDX contributors
# SPDX-License-Identifier: Apache-2.0

# The SPDX 3 support depends on the optional `spdx-python-model` bindings, which
# are not installed by default and currently cannot be built from git on Windows.
# When the bindings are unavailable, skip collecting the SPDX 3 test suite instead
# of failing at import time.
try:
    import spdx_python_model  # noqa: F401
except ImportError:
    collect_ignore_glob = ["*"]
