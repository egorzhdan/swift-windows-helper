import sys
import os

toolchain_path = sys.argv[1]  # C:\Library\Developer\Toolchains\unknown-Asserts-development.xctoolchain
print("Patching toolchain at", toolchain_path)
rel_path = "\\usr\\lib\\swift\\windows\\x86_64"

sdks_path = "C:\\Program Files (x86)\\Windows Kits\\10\\Include"
sdk_path = sdks_path + "\\" + max(os.listdir(sdks_path))
print("Found Windows SDK at", sdk_path)

vcs_path = "C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\VC\\Tools\\MSVC"
vc_path = vcs_path + "\\" + max(os.listdir(vcs_path)) + "\\include"
print("Found VC at", vc_path)

symlink_path = toolchain_path + rel_path + "\\winsdk"
vc_symlink_path = toolchain_path + rel_path + "\\vc"

print("Creating symlinks at", symlink_path, vc_symlink_path)
os.system("mklink /d \"" + symlink_path + "\" \"" + sdk_path + "\"")
os.system("mklink /d \"" + vc_symlink_path + "\" \"" + vc_path + "\"")

modulemap_path = toolchain_path + rel_path + "\\glibc.modulemap"
print("Creating modulemap at", modulemap_path)
visualc_modulemap = open(toolchain_path + rel_path + "\\visualc.modulemap", "r").read()
winsdk_modulemap = open(toolchain_path + rel_path + "\\winsdk.modulemap", "r").read()
ucrt_modulemap = open(toolchain_path + rel_path + "\\ucrt.modulemap", "r").read()

f = open(modulemap_path, "w")
f.write(visualc_modulemap.replace("header \"", "header \"vc/") +
        winsdk_modulemap.replace("header \"", "header \"winsdk/um/") +
        ucrt_modulemap.replace("header \"", "header \"winsdk/ucrt/"))
f.close()

print()
print("Done!")
