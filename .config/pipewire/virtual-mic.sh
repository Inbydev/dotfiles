#!/bin/bash

# Cargar el módulo de loopback para los dos micrófonos
pactl load-module module-null-sink sink_name=combined_mic sink_properties=device.description=Combined_Microphone

# Combinar las entradas de los dos micrófonos reales en uno virtual, con 20ms de retraso en el primero
loopback1=$(pactl load-module module-loopback source=alsa_input.usb-Kingston_HyperX_QuadCast_S_4100-00.analog-stereo sink=combined_mic)
loopback2=$(pactl load-module module-loopback source=pipewire-screenaudio sink=combined_mic latency_msec=20)

# Ajustar el volumen de cada micrófono
# 65536 es el valor máximo (100%), así que 40% sería 26214

# Ajustar el volumen del primer micrófono al 100%
pactl set-source-volume alsa_input.usb-Kingston_HyperX_QuadCast_S_4100-00.analog-stereo 140%

# Ajustar el volumen del segundo micrófono al 40%
pactl set-source-volume pipewire-screenaudio 40%
