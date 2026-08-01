commands = input("Input Command: (MOVE, ADD , STORE, SUBTRACT)") 
if commands not in ("MOVE", "ADD", "STORE", "SUBTRACT"):
    print(f"ERROR_INVALIDCOMMAND_ERROR_ID_2 ~~~ {commands} INVALID ID ")
data = int(input("Input data amount: (0-180)"))
if data > 180 or data <= 0:
    print(f"ERROR_OUTOFRANGE_ERROR_ID_1 ~~~ {data} OUT OF RANGE ")
header = "ARD99"

print("===========")
print(f"COMMAND: {commands} ")
print(f"DATA: {data}")
print(f"HEADER: {header}")
print("===========")