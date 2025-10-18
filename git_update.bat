@echo off
echo Updating GitHub repository...

git add .
git commit -m "Update README with comprehensive project information"
git push origin main

echo.
echo GitHub repository updated!
pause
