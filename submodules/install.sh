set -eux
cd "$(git rev-parse --show-toplevel)"
git submodule update --init
[ ! -d submodules/go ] && mkdir submodules/go
