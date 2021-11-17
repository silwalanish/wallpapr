#!/bin/sh

# Stop services if they are running.
WALLPAPR_TIMER_STATUS=$(systemctl --user is-active wallpapr.timer)
WALLPAPR_SERVICE_STATUS=$(systemctl --user is-active wallpapr.service)

if [[ $WALLPAPR_TIMER_STATUS == "active" ]]; then
  systemctl --user stop wallpapr.timer;
  systemctl --user disable wallpapr.timer;
fi

if [[ $WALLPAPR_SERVICE_STATUS == "active" ]]; then
  systemctl --user stop wallpapr.service;
  systemctl --user disable wallpapr.service;
fi

# Export the secrets
mkdir -p ~/.config/environment.d/
rm -f -- ~/.config/environment.d/wallpapr.conf
printf "UNSPLASH_ACCESS_KEY=\"${UNSPLASH_ACCESS_KEY}\"\nUNSPLASH_SECRET_KEY=\"${UNSPLASH_SECRET_KEY}\"\n" >> ~/.config/environment.d/wallpapr.conf

# Install wallpapr service.
mkdir -p ~/.config/systemd/user/

cp wallpapr.service ~/.config/systemd/user
systemctl --user start wallpapr.service
systemctl --user enable wallpapr.service

cp wallpapr.timer ~/.config/systemd/user
systemctl --user start wallpapr.timer
systemctl --user enable wallpapr.timer
