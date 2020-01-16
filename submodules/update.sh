#!/bin/sh
set -eux
cd "$(git rev-parse --show-toplevel)"
git pull --rebase
git submodule update --init --recursive
git submodule foreach git pull --rebase origin master
git add submodules
git diff-index --quiet --cached HEAD || {
  git commit -m "[submodules] bump submodules (automated)"
  git show
}
