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

# Remove service and configurations.
rm -f -- ~/.config/systemd/user/wallpapr.service
rm -f -- ~/.config/systemd/user/wallpapr.timer
rm -f ~/.config/environment.d/wallpapr.conf
rm -rf ~/.config/wallpapr
