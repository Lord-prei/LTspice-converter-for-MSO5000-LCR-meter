# Lib for all the TEMP stuff

import  sys
import  os

# --------------------------------------------------------------------------- define Paths

# define Paths
# region Paths

if getattr(sys, "frozen", False):
    # Running as PyInstaller EXE
    Base_Dir =  os.path.dirname(sys.executable)
    Lib_Dir =   os.path.join(Base_Dir, "Lib")
else:
    # Running as normal Python script
    Lib_Dir =   os.path.dirname(os.path.abspath(__file__))
    Base_Dir =  os.path.dirname(Lib_Dir)

Settings_Path = os.path.join(Base_Dir, "Settings")
Data_Path =     os.path.join(Base_Dir, "Data")

# endregion Paths

# ---------------------------------------------------------------------------
# Here Come all of the Functions
# region Functions

# -------------------------------------------------- Layer 1

# Functions Layer 1
# region Functions Layer 1

# Code for Functions Layer 1

# endregion Functions Layer 1

# -------------------------------------------------- Layer 2

# Functions Layer 2
# region Functions Layer 2

# Code for Functions Layer 2

# endregion Functions Layer 2

# -------------------------------------------------- Layer 3

# Functions Layer 3
# region Functions Layer 3

# Code for Functions Layer 3

# endregion Functions Layer 3

# endregion Functions
# --------------------------------------------------------------------------- 
# ----------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Here Come all of the Functions
# region Functions

# -------------------------------------------------- Layer 1

# Functions Layer 1
# region Functions Layer 1

# Code for Functions Layer 1

# endregion Functions Layer 1

# -------------------------------------------------- Layer 2

# Functions Layer 2
# region Functions Layer 2

# Code for Functions Layer 2

# endregion Functions Layer 2

# -------------------------------------------------- Layer 3

# Functions Layer 3
# region Functions Layer 3

# Code for Functions Layer 3

# endregion Functions Layer 3

# endregion Functions
# --------------------------------------------------------------------------- 