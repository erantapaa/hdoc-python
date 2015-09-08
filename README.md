
Simple python script to open a package's documentation index on Hackage.

E.g.:

    hdoc binary
    hdoc modular-a     # opens docs for modular-arithmetic
    hdoc odular-a      # same effect

You only need to type a unique substring (case-insensitive) of
the package name. `hdoc` will list all matching package names
if the substring is not unique.

