import sys
import shutil

sdk_path = sys.argv[1]  # C:\Library\Developer\Platforms\Windows.platform\Developer\SDKs\Windows.sdk
dispatch_dir = sdk_path + "\\usr\\lib\\swift\\dispatch"
include_dir = sdk_path + "\\usr\\include"
shutil.move(dispatch_dir, include_dir)
