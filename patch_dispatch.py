import sys
import shutil

sdk_path = sys.argv[1]  # C:\Library\Developer\Platforms\Windows.platform\Developer\SDKs\Windows.sdk

include_dir = sdk_path + "\\usr\\include"

dir_names = [
    "Block",
    "dispatch",
    "os",
]

for dir_name in dir_names:
    current_dir = sdk_path + "\\usr\\lib\\swift\\" + dir_name
    print("Moving", current_dir, "to", include_dir)
    shutil.move(current_dir, include_dir)

print()
print("Done!")
