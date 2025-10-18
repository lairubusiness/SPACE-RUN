@echo off
echo Setting up Git for SPACE RUN...

git config user.name "SPACE-RUN"
git config user.email "spacerun@game.dev"

echo Committing files...
git commit -m "Initial commit: SPACE RUN Game with Character Development"

echo Adding remote repository...
git remote add origin https://github.com/lairubusiness/SPACE-RUN.git

echo Renaming branch to main...
git branch -M main

echo Pushing to GitHub...
git push -u origin main

echo.
echo Done! Your game is uploaded to GitHub!
pause
