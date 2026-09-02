#!/bin/bash
python -m venv ./.venv
./.venv/bin/pip install yt_dlp --upgrade
./.venv/bin/python main.py
