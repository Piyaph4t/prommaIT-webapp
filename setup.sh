#!/bin/bash
get_pkg_manager() {
    for pm in apt dnf yum pacman zypper; do
        if command -v $pm >/dev/null 2>&1; then
            echo "$pm"
            return
        fi
    done
    echo "unknown"
    exit 1
}
PACKAGE_MANAGER=$(get_pkg_manager)
echo "Package manager: $PACKAGE_MANAGER"


# Update system
sudo $PACKAGE_MANAGER update -y && sudo $PACKAGE_MANAGER upgrade -y

# Install packages
INSTALL="sudo $PACKAGE_MANAGER install -y"
$INSTALL python3 python3-venv python3-pip


echo "✅ Virtual environment created."

source venv/bin/activate
pip install -r requirements.txt
echo ""
echo "🎉 SETUP COMPLETE!"
echo "------------------------------------------------"
echo "To start your server, run these commands:"
echo ""

echo "python3 run.py"
echo ""

echo "------------------------------------------------"
