#!/bin/sh

set -eu

cd "$(dirname "$0")"

needs_sudo () {
  site_packages=$(python -c 'import site; print site.getsitepackages()[0]')
  test -w "$site_packages"
}

maybe_sudo () {
  if needs_sudo; then
    sudo "$@"
  else
    "$@"
  fi
}

if ! which pip >/dev/null 2>&1; then
  curl -O https://bootstrap.pypa.io/get-pip.py
  maybe_sudo python get-pip.py
fi

if ! which virtualenv >/dev/null 2>&2; then
  maybe_sudo pip install virtualenv
fi

virtualenv pyenv
. pyenv/bin/activate
pip install -r requirements.txt
