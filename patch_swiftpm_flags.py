import sys

platform_path = sys.argv[1]  # C:\Library\Developer\Platforms\Windows.platform
print("Patching platform at", platform_path)

info_plist_path = platform_path + "\\Info.plist"

f = open(info_plist_path, "r")
info_plist = f.read()
f.close()

flags = """
<string>-I</string>
<string>{platform}\\Developer\\SDKs\\Windows.sdk\\usr\\include</string>

<string>-I</string>
<string>{platform}\\Developer\\SDKs\\Windows.sdk\\usr\\lib\\swift</string>

<string>-I</string>
<string>{platform}\\Developer\\SDKs\\Windows.sdk\\usr\\lib\\swift\\windows</string>

<string>-L</string>
<string>{platform}\\Developer\\SDKs\\Windows.sdk\\usr\\lib\\swift\\windows</string>
""".format(platform=platform_path)

f = open(info_plist_path, "w")
f.write(info_plist.replace("<array>", "<array>" + flags))
f.close()

print()
print("Done!")
