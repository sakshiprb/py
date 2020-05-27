# py
Python practise


How to Git

git clone https://github.com/sakshiprb/py.git
Cloning into 'py'...

got to repo dir

D:\Softwares\Sublime Text 3>cd py

Check git status

D:\Softwares\Sublime Text 3\py>git status
On branch master
Your branch is up to date with 'origin/master'.

D:\Softwares\Sublime Text 3\py>git checkout -b dev
Switched to a new branch 'dev'


D:\Softwares\Sublime Text 3\py>git status
On branch dev
Untracked files:
  (use "git add <file>..." to include in what will be committed)

        pg.py
        pg1.py

nothing added to commit but untracked files present (use "git add" to track)

To add single file

D:\Softwares\Sublime Text 3\py>git add pg.py

To add all files

D:\Softwares\Sublime Text 3\py>git add -A


D:\Softwares\Sublime Text 3\py>git commit -m "My first checkin for leetcode"
[dev 6e15900] My first checkin for leetcode


D:\Softwares\Sublime Text 3\py>git push
fatal: The current branch dev has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin dev


D:\Softwares\Sublime Text 3\py>git push --set-upstream origin dev
Enumerating objects: 5, done.
