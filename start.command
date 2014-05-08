#!/bin/sh

set -eu

cd "$(dirname "$0")"

export VIRTUAL_ENV="$PWD/pyenv"
export PATH="$VIRTUAL_ENV/bin:$PATH"
export PS1="\h:\W \u\$ "
unset PYTHON_HOME

if [ "$SHELL" != "/bin/bash" ]; then
  echo
  echo "You've customized your \$SHELL, so this might not work. Seeing as you"
  echo "probably know what you're doing, I suggest you just open this directory"
  echo "in your shell of choice and run:"
  echo
  echo "    . pyenv/bin/activate"
  echo
fi

python testenv.py

exec "$SHELL"
