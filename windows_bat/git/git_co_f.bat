@echo off

echo %cd%
for /r %cd% %%i in (.git) do (	if exist %%i (
			echo %%i
			cd %%i 
			cd ..
			git co -f 
		)
	)
