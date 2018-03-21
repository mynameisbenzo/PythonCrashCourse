# adding whitespace is fine, but what about taking whitespace out?
favLanguage = 'python '

# whether you see it or not, that space at the end of python is currently being printed
print(favLanguage)

# let's strip that space with rstrip()
favLanguage = favLanguage.rstrip()

# now instead of printing 'python ', we are currently printing 'python'
print(favLanguage)

# using lstrip()
favLanguage = ' python'
favLanguage = favLanguage.lstrip()

# will print 'python' not ' python'
print(favLanguage)

# using strip()
favLanguage = ' python'
favLanguage = favLanguage.strip()

# will print 'python' not ' python '
print(favLanguage)