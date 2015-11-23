set -eux
cd "$(git rev-parse --show-toplevel)"
git submodule init
git submodule update
[ ! -e submodules/ministat/src/ministat ] && ( cd submodules/ministat &&
  ./configure &&
  make
)
