# prüfen
ls -al ~/.ssh
ssh-add -l

# neuen Key erzeugen
ssh-keygen -t ed25519 -C "deine.email@beispiel.de"

# ssh-agent starten & Key hinzufügen
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# öffentlichen Key kopieren (macOS / Linux / Windows)
cat ~/.ssh/id_ed25519.pub
pbcopy < ~/.ssh/id_ed25519.pub    # macOS (wenn verfügbar)
xclip -sel clip < ~/.ssh/id_ed25519.pub  # Linux mit xclip
clip < ~/.ssh/id_ed25519.pub     # Git Bash on Windows

# Verbindung testen
ssh -T git@github.com

# klonen
git clone git@github.com:owner/repo.git

# vorhandenes Repo auf SSH umstellen
git remote set-url origin git@github.com:owner/repo.git

# push/pull basics
git add .
git commit -m "msg"
git push origin branch-name
git pull origin branch-name

