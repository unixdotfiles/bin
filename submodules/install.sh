set -eux
cd "$(git rev-parse --show-toplevel)"
git submodule update --init
[ ! -e submodules/ministat/src/ministat ] && (
  cd submodules/ministat &&
  ./configure &&
  make
)
[ ! -d submodules/go ] && mkdir submodules/go
(
  export GOPATH=~/bin/submodules/go/ &&
  go get -d -u github.com/google/battery-historian/...
)
