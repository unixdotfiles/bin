set -eux
cd "$(git rev-parse --show-toplevel)"
git submodule update --init
[ ! -e submodules/ministat/src/ministat ] && (
  cd submodules/ministat &&
  ./configure &&
  make
)
[ ! -d submodules/go ] && mkdir submodules/go
