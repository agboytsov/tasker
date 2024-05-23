#!/bin/bash
cd app
flask db upgrade
python app.py