#!/bin/bash
git clone $REPO_URL ok && cd ok && pip3 install -U -r requirements.txt
$python -m mbot
