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
yay -S --needed hyprpaper-git \
hyprland-git \
hyprland-protocol-git \
hyprgraphics-git \
waybar \
bibata-cursor-theme \
eza \
kitty \
grim \
slurp \
waybar \
wofi \
wttrbar-git \
xdg-desktop-portal-hyprland-git \
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
fastfetch \
xnviewmap \
librewolf-bin \
fzf \
libreoffice-fresh \
noto-fonts \
noto-fonts-cjk \
noto-fonts-emoji \
7zip \
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
