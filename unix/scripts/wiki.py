import wikipedia

print(wikipedia.summary("unix philosophy", sentences=3))

print("---")

print(wikipedia.page("unix philosophy").section("Origin"))
