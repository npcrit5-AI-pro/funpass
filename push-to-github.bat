@echo off
echo ========================================
echo   Push FunPass to GitHub
echo ========================================
echo.
echo Follow these steps:
echo.
echo 1. Go to https://github.com/new
echo 2. Create a repository named: funpass
echo 3. Do NOT initialize with README, .gitignore, or license
echo 4. Copy the remote URL (should be: https://github.com/npcrit5-AI-pro/funpass.git)
echo.
pause
echo.
echo Enter the remote URL (or press Enter for default):
set /p REMOTE_URL=
if "%REMOTE_URL%"=="" set REMOTE_URL=https://github.com/npcrit5-AI-pro/funpass.git
echo.
echo Adding remote and pushing to GitHub...
git remote add origin %REMOTE_URL%
git branch -M main
git push -u origin main
echo.
echo ========================================
echo   Done! Your repo is on GitHub!
echo ========================================
pause
