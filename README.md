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
yay -S --needed hyprpaper \
hyprland \
ags-hyprpanel-git \
hyprpicker \
swww \
bibata-cursor-theme \
eza \
kitty \
grim \
slurp \
wofi \
xdg-desktop-portal-hyprland \
xdg-utils \
zoxide \
zsh \
```

## Apps I use

```bash
yay -S --needed 7zip \
aegisub-arch1t3cht-git \
android-studio \
android-tools \
bibata-cursor-theme \
bottom \
cava \
clamav \
cpupower-gui \
cuda \
docker \
docker-compose \
dosfstools \
downgrade \
dupeguru \
dust \
easyeffects \
fastfetch \
fdupes \
freetube \
fzf \
git \
github-cli \
gitleaks \
gradle \
grim \
imagemagick \
jdk17-openjdk \
kdenlive \
krita \
kronometer \
libreoffice-fresh \
librewolf-bin \
linux-firmware \
linux-hardened \
linux-hardened-headers \
lxappearance \
man-db \
moc-pulse \
mpv \
nano \
nautilus \
networkmanager \
nicotine+ \
noto-fonts \
noto-fonts-cjk \
noto-fonts-emoji \
ntfs-3g \
nvidia-open-dkms \
obsidian \
openrazer-daemon \
pavucontrol \
picard \
pipewire-alsa \
pipewire-pulse \
pnpm \
polychromatic \
protonmail-bridge-bin \
qalculate-gtk \
reflector \
rustup \
schildichat-desktop-bin \
slurp \
smartmontools \
spek \
syncthing \
tenacity \
thunderbird \
ufw \
unrar \
woff2 \
wofi \
xdg-desktop-portal-gtk \
xnviewmp \
yazi \
yt-dlp \
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
