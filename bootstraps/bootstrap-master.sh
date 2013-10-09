#!/usr/bin/env bash

sudo -i

# docker run samalba/docker-registry

echo "[Unit]
Description=Docker registry
After=docker.service

[Service]
Restart=always
ExecStart=/usr/bin/docker run samalba/docker-registry

[Install]
WantedBy=local.target
" >> /media/state/units/docker-registry.service

systemctl restart local-enable.service

# finish with logout (exit)
#exit