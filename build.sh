#!/bin/bash

SCRIPT="proxymain.py"
OUTPUT_NAME="ProxyCheckerTool"
ICON_FILE="./i.ico"

echo "🔧 Building executable for $SCRIPT..."

rm -rf build dist __pycache__

pyinstaller --onefile \
    --name "$OUTPUT_NAME" \
    --icon "$ICON_FILE" \
    --hidden-import=requests \
    --hidden-import=urllib3 \
    --hidden-import=bs4 \
    --hidden-import=colorama \
    --collect-all=requests \
    --collect-all=urllib3 \
    --clean \
    "$SCRIPT"

if [ -f "dist/$OUTPUT_NAME" ]; then
    echo "✅ Build successful! Executable created in: dist/$OUTPUT_NAME"
    echo "🚀 To run: ./dist/$OUTPUT_NAME"
else
    echo "❌ Build failed!"
    exit 1
fi
