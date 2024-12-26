# Packages

## yay

For install AUR packages [Tutorial Followed](https://itsfoss.com/install-yay-arch-linux/)


```
sudo pacman -Syu
```

```
sudo pacman -S --needed base-devel git
```

```
git clone https://aur.archlinux.org/yay.git
```

```
cd yay
```

```
makepkg -si
```

## For Appeareance

```
yay -S --needed hyprpaper \
hyprland \
hyprgraphics-git \
waybar \
bibata-cursor-theme \
eza \
kitty \
sddm \
simple-sddm-theme-git \
grim \
slurp \
waybar \
wofi \
wttrbar \
xdg-desktop-portal-hyprland \
xdg-utils \
zoxide \
zsh \
```

## Apps I use

```
yay -S --needed bottom \
docker \
docker-compose \
deepin-calculator \
eog \
fastfetch \
librewolf-bin \
fzf \
libreoffice-fresh \
noto-fonts \
noto-fonts-cjk \
noto-fonts-emoji \
p7zip \
pavucontrol \
usbutils
```

# Usage

Ensure you have the following installed on your system

## Git

```
pacman -S git
```

## Stow

```
pacman -S stow
```

# Installation

First, check out the dotfiles repo in your $HOME directory using git

```
$ git clone https://github.com/Inbydev/dotfiles.git
$ cd dotfiles
```

then use stow to create symlinks

```
$ stow .
```
