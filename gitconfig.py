import os
import subprocess

UPSTREAM_REPO = os.environ.get('UPSTREAM_REPO', "https://github.com/risswazowlsky/Zen-Robot")
try:
    if len(UPSTREAM_REPO) == 0:
       raise TypeError
except TypeError:
    UPSTREAM_REPO = None

if UPSTREAM_REPO is not None:
    if os.path.exists('.git'):
        subprocess.run(["rm", "-rf", ".git"])

    subprocess.run([f"git init -q \
                      && git config --global user.email chika@kaguyasama.corp \
                      && git config --global user.name chika \
                      && git add . \
                      && git commit -sm update -q \
                      && git remote add origin {UPSTREAM_REPO} \
                      && git fetch origin -q \
                      && git reset --hard origin/master -q"], shell=True)
