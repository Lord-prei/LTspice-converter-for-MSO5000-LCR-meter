# ----------------------------------------------------------------------------------------------------
#       Project: LTspice converter for MSO5000 LCR meter
#       Purpose: Exporting data and converting it to format for my programm to test the LCR meter
#       Version: V0.0.1
# ----------------------------------------------------------------------------------------------------
#       Version control
# --------------------------------------------------------------------------- Copypaste
#
#       VERSIONNAME
#
#       JJJJMMDD, MODIFICATION, Vx.x.x, LZerres:
#           CHANGE 1
#           CHANGE 2
#           CHANGE 3
#
# --------------------------------------------------------------------------- Vx.x.x

import  sys
import  os
import  ltspice
import  numpy as np
import  pandas as pd
from    enum        import Enum
import  Lib.Input as I
import  Lib.Process as P
import  Lib.Output as O

VERSION_SW = "0.0.1"  

print(f"\x1b]0;LTspice conv V{VERSION_SW}\x07") # Added Version Number to be displayed in CLI title

# --------------------------------------------------------------------------- Variables



# --------------------------------------------------------------------------- Constants


class constants(Enum):
    temp = 0

    # Random ah


# --------------------------------------------------------------------------- define Paths

# define Paths
if getattr(sys, "frozen", False):
    Base_Dir =  os.path.dirname(sys.executable)
else:
    Base_Dir =  os.path.dirname(os.path.abspath(__file__))

Data_Path =     os.path.join(Base_Dir, "Data")

# --------------------------------------------------------------------------- Init

rawFile = os.path.join(Data_Path, "simulation.raw")
l = ltspice.Ltspice(rawFile)
l.parse()

# ---------------------------------------------------------------------------------------------------- Functions
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

# --------------------------------------------------------------------------- Main Loop

# while True:  # Main Loop

freq  = l.get_frequency()
print(l.variables)
