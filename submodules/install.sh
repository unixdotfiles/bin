set -eux
cd "$(git rev-parse --show-toplevel)"
git submodule init
git submodule update
( cd submodules/ministat &&
  ./configure &&
  make
)
