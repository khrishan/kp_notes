# Git Notes
So as a "Computer Science Graduate", I should be very familiar with Git and GitHub. But honestly, __I wasn't__. Everytime I used Git, it was always through the website or through the "Github for Desktop" application.

I really wanted to know how to use it 'properly' - which for me is through the command line.

Below are my notes, that I made whilst going over the topic. It contains the most important commands and what they do / mean.

Enjoy :) 

## Contents
+ [Introduction](#introduction)
+ [Using Git](#using-git)
+ [Track a Directory](#track-a-directory)
+ [Track Files](#track-files)
+ [Ignore Files](#ignore-files)
+ [Commit Files](#commit-files)
+ [Remove Files](#remove-files)
+ [Log Commit History](#log-commit-history)
+ [Undoing a Commit](#undoing-a-commit)
+ [Creating a New Repository](#creating-a-new-repository)
+ [Push an Exisiting Repository](#push-an-existing-repository)
+ [Pull Files](#pull-files)
+ [Commit to GitHub](#commit-to-github)
+ [Aliases](#aliases)
+ [Clone Repositories](#clone-repositories)
+ [Remove Tracked Files](#remove-tracked-files)
+ [Branching Commits](#branching-commits)
+ [Merge Conflicts](#merge-conflicts)
+ [Delete Branch](#delete-branch)
+ [Reverting vs Resetting](#reverting-vs-resetting)

## Introduction

In Git, files transition between 3 states with Git

1. Modified Files are files that have been recently changed
2. Staged Files have been marked to be saved
3. Committed Files are those that have been saved

Git saves all file changes to a directory as a compressed database. 

1. You modify files in Working Directory
2. You notify that want to save changes in your Staging Area
3. After you Commit the file changes are saved in the Git directory

## Using Git

`git config --global user.name "Khrishan Patel"` 

`git config --global user.email "test@test.com`

`git config --global core.editor "vim"` -  Set editor as vim

`git config --list` -  Show all the settings

`git help` OR `git help <COMMAND>`

`git status` - Shows the state of your files meaning if they are tracked, have been modified and the branch your on

_To edit the `.gitconfig` file, then cd to root (`~`), then `vim .gitconfig' and then edit away!_

## Track a Directory

1. Go to directory
2. `git init`  - Creates the `.git` directory

## Track Files

+ By type : `git add *.java`
+ By name : `git add AndroidManifest.xml`
+ Track all files : `git add .`

## Ignore Files

Create a `.gitignore` file. Link to file can be found [here](https://github.com/github/gitignore)

## Commit Files
`git commit -m 'Initial project version'` - Commits the changes and sets an abbreviated commit message
the branch your on.

`git commit` - Opens the editor we defined above

Type a message that reflects the committed. Try to follow the following format (6 Steps): 

+ Type a **heading** that briefly explains the changes __(50 characters or less)__
+ Describe the **original problem** that is being addressed
+ Describe the **specific change** being made
+ Describe the **result** of the change
+ Describes any **future** improvements
+ Post a **__closed bug__** notation e.g. `Closed-Bug: #1291621`

OR

`git commit -a -m `'<COMMENT>'` - Skips staging and commit message

## Remove Files

`rm <FILENAME>` - If you remove a file it shows as `Changed but not updated`

`git rm <FILENAME>` - How to remove the actual file

If you have committed a file to be removed you must add the `-f` option

`git rm --cached <FILENAME>` - Keep file, but remove from staging area

`git mv <FILENAME>` - Renames a file

## Log Commit History

`git log` - Shows all of the previous commit messages in reverse order

`git log --pretty=oneline` - Shows commits on one line

`git log --pretty=format:"%h : %an : %ar : %s` 

| Key        | Description |
| :--------: |:-----------:|
| `%h` | Abbreviated Hash |
| `%an` | Author's Name |
| `%ar` | Date Changed |
| `%s`| First line of Comment |


`git log -p -2` - Shows the last 2 commit changes

`git log --stat` - Prints abbreviated stats

`git log --since=1.weeks` - Show only changes in the last week

`git log --since="2014-04-12"` - Show changes since this date

`git log --author="Derek Banas"` - Changes made by author

`git log --before="2014-04-13"` - Changes made before this date

## Undoing a Commit

`git commit --amend` - If you want to change your previous commit

# GitHub

## Creating a new repository
First create a new repository on [github.com](https:www.github.com) then to create the repository on your machine then do the following : 
```
touch README.md
git init
git add README.md
git commit -m 'Inital Commit'
git remote add origin <URL OF GIT REPOSITORY>
git push -u origin master

```
*NB : What this does is perform an initial commit by committing the README.md file*

## Push an exisiting repository
`git remote add origin <URL OF GIT REPOSITORY>`

`git push -u origin master`

Then it will ask for you username and password in order to continue.

## Pull files
`git remote -v` - pull files and make changes

`git pull <URL>` - get a file and get that uploaded

## How to update to Github

```
git add <FILE>
git commit -m '<MESSAGE>
git push
```

## Aliases

Shotcut ways to do a lot of things - For example change 'git commit' to something else

`git config --global alias.co commit`

now becomes

`git co -m '<MESSAGE>`

## Clone Repositories

First, find a repository then fork it (inside of GitHub). Copy the URL and then 
change directory to where you want the files.

`git clone URL <URL>`

## Remove Tracked Files
 
`git rm -r --cached '<NAME OF FILE>'|.` - Gets rid of specific files
`git reset` - Gets rid of everything (from the cached area)

Then, commit the `.gitignore` file then add files to git!
 
## Branching Commits
 
Branching allows us to take the project our own way so we do not effect the main project.
 
default branch = Master
 
Use pointer called `HEAD` - use command called `checkout` in order to change where `HEAD` is pointing to.

`git checkout <NAME OF BRANCH>`
 
## Merge Conflicts
 
`git branch <NAME OF BRANCH>`
`git checkout <NAME OF BRANCH>`
 
`git checkout -b <NAME OF BRANCH>` (Shorthand version)
 
`git checkout -b <NAME OF BRANCH> origin/<NAME OF BRANCH>`

`get branch` - see all branches

`git branch --merged` - see those branches that have been merged into the master branch / that are up to date with the master branch.

`git branch --no-merged` - see those that are not in sync with the master branch

`git branch -v`  (* indicates where current branch)
 
`git merge <NAME OF BRANCH>`
 
## Delete branch
`git branch -d <NAME OF BRANCH>` deletes branch locally
 
`git branch -D <NAME OF BRANCH>` - remove branch that hasn't been merged yet locally (the capital `D` is like a 'force' through.
 
To then delete branch on GitHub
`git push origin :<NAME OF BRANCH>` (ensure no space between colon and name)

`git branch -m <NAME OF NEW BRANCH>` - Change name of branch
 
## Fixing Merge Requests

Do that on GitHub - everyone else does!

There may be a case where you are working on a branch, and you get left behind from the master...

This is resolved by __rebasing__ - moves a branch to new base (fast forward merge)
 
`git rebase master`
 
## Reverting vs Resetting
 
`revert` - undoes changes done in that commit : it creates a new commit that eliminates changes made in earlier commit
 
'git revert HEAD' - then change message to show what you have done
 
`reset` - actually deletes the commit

`git reset`  - reset the staging area
`git rest` <NAME OF COMMIT>
`git reset --hard` - resets staging area and changes working directory to match most recent commit
`git reset --hard <NAME OF COMMIT>`

__N.B : RESET is bad practice - try to avoid at all cost!!!__
