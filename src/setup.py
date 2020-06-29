#Creating executable version of the game Tanks
import cx_Freeze


executables = [cx_Freeze.Executable("Tanks.py", icon = "Icons/tankico.ico")]

#packaging executable
cx_Freeze.setup(
	name = "Tanks",
	options={"build_exe":{"packages":["pygame"],
						 "include_files":["Images"]}},
	executables = executables,
	)
