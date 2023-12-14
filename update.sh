#!/usr/bin/env bash
systemctl stop mcwipe
git pull
systemctl start mcwipe