#!/bin/bash

# Polychromatic Configs
# Mouse
polychromatic-cli -s PM2116H15001188 --dpi 1000
# Keyboard
polychromatic-cli -s PM2131F59800107 -o keyswitch_optimisation -p True
polychromatic-cli -s PM2131F59800107 -o poll_rate -p 8000
polychromatic-cli -s PM2131F59800107 -e no-lights
