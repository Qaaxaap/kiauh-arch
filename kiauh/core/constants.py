# ======================================================================= #
#  Copyright (C) 2020 - 2026 Dominik Willner <th33xitus@gmail.com>        #
#                                                                         #
#  This file is part of KIAUH - Klipper Installation And Update Helper    #
#  https://github.com/dw-0/kiauh                                          #
#                                                                         #
#  This file may be distributed under the terms of the GNU GPLv3 license  #
# ======================================================================= #

import os
import pwd
from pathlib import Path
from typing import Dict

# global dependencies
GLOBAL_DEPS = ["git", "wget", "curl", "unzip", "dfu-util", "python3-virtualenv"]

# Debian to Arch Linux package name mappings
DEBIAN_TO_ARCH_PACKAGES: Dict[str, str] = {
    "python3-virtualenv": "python-virtualenv",
    "python3-numpy": "python-numpy",
    "python3-matplotlib": "python-matplotlib",
    "libopenblas-dev": "openblas",
    "python3-pip": "python-pip",
    "python3-dev": "python",
    "libyaml-dev": "libyaml",
    "build-essential": "base-devel",
    "python3-setuptools": "python-setuptools",
    "avahi-daemon": "avahi",
    "dpkg-dev": "base-devel",
    "libffi-dev": "libffi",
    "libssl-dev": "openssl",
}

# strings
INVALID_CHOICE = "Invalid choice. Please select a valid value."

# current user
CURRENT_USER = pwd.getpwuid(os.getuid())[0]

# dirs
SYSTEMD = Path("/etc/systemd/system")
def _detect_arch() -> bool:
    try:
        with open("/etc/os-release") as f:
            content = f.read()
        ids = set()
        for line in content.splitlines():
            if line.startswith("ID=") or line.startswith("ID_LIKE="):
                ids.update(line.split("=", 1)[1].strip('"').lower().split())
        return "arch" in ids
    except Exception:
        return False


_IS_ARCH = _detect_arch()

if _IS_ARCH:
    NGINX_SITES_AVAILABLE = Path("/etc/nginx/conf.d")
    NGINX_SITES_ENABLED = Path("/etc/nginx/conf.d")
    NGINX_CONFD = Path("/etc/nginx/conf.d")
else:
    NGINX_SITES_AVAILABLE = Path("/etc/nginx/sites-available")
    NGINX_SITES_ENABLED = Path("/etc/nginx/sites-enabled")
    NGINX_CONFD = Path("/etc/nginx/conf.d")
