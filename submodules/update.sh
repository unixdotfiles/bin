set -eux
cd "$(git rev-parse --show-toplevel)"
git submodule init
git submodule update
git submodule foreach git pull --rebase origin master
