set -eux
cd "$(git rev-parse --show-toplevel)"
git submodule update --init
[ ! -e submodules/ministat/src/ministat ] && (
  cd submodules/ministat &&
  ./configure &&
  make
)
[ ! -d submodules/go ] && mkdir submodules/go
[ ! -e submodules/check-soa/check-soa ] &&
(
  export GOPATH=~/bin/submodules/go/ &&
  go get github.com/miekg/dns &&
  (cd submodules/check-soa && go build check-soa.go)
)
