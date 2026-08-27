#!/data/data/com.termux/files/usr/bin/bash

clear

echo "======================================"
echo "   Telegram Backup Uploader Setup"
echo "======================================"
echo ""

echo "[1/4] Updating packages..."
pkg update -y

echo ""
echo "[2/4] Upgrading packages..."
pkg upgrade -y

echo ""
echo "[3/4] Installing required packages..."
pkg install python git -y

echo ""
echo "[4/4] Installing Python library..."
pip install -U python-telegram-bot

clear

echo "======================================"
echo "   Installation Completed!"
echo "======================================"
echo ""

echo "Next steps:"
echo ""
echo ">> Configure config.py"
echo ""
echo ">> Add your Bot Token"
echo ""
echo ">> Add your Telegram Channel ID"
echo ""
echo ">> Then run:"
echo ""
echo "   python backup.py"
echo ""

echo "======================================"
