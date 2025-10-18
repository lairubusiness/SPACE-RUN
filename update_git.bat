@echo off
echo Updating GitHub repository...
git add .
git commit -m "Update: Add git push script and web assets"
git push origin main
echo.
echo ✅ Repository updated successfully!
pause
