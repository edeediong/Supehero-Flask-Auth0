#!/bin/bash

cp -rf /app/bulma.service /etc/systemd/system/
systemctl daemon-reload
systemctl start bulma
systemctl enable bulma
systemctl status bulma
systemctl restart bulma