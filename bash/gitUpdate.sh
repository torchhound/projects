#!/bin/bash

echo "Enter the complete path to the git repository:"
read repo
cd $repo
git fetch upstream
git checkout master 
git merge upstream master
git add .
git commit -m "Updated $repo to upstream"
git push -u origin master
exit 0