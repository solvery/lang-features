@echo off

timeout /t 60

echo %cd%
for /r %cd% %%i in (.git) do (	if exist %%i (
			echo %%i
			cd %%i 
			cd ..
			git svnup
		)
	)
