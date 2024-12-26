# Packages

## yay

For install AUR packages [Tutorial Followed](https://itsfoss.com/install-yay-arch-linux/)


```bash
sudo pacman -Syu
```

```bash
sudo pacman -S --needed base-devel git
```

```bash
git clone https://aur.archlinux.org/yay.git
```

```bash
cd yay
```

```bash
makepkg -si
```

## For Appeareance

```bash
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

```bash
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

## Git and Stow

```bash
pacman -S --needed git stow
```

# Installation

First, check out the dotfiles repo in your $HOME directory using git

```bash
git clone https://github.com/Inbydev/dotfiles.git
cd dotfiles
```

then use stow to create symlinks

```bash
stow .
```
