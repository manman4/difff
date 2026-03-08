#!/bin/bash
cd "$(dirname "$0")"
echo "difff を起動します: http://localhost:8080/"
echo "終了するには Ctrl+C を押してください"
python3 server.py
