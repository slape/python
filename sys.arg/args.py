import sys
#print(sys.argv[0], sys.argv[1])
# Getting help with '--help' or -h
if sys.argv[1] == '--help' or sys.argv[1] == '-h':
    out = """
    Usage: args [options] [file]
    '-s' Salamander. Turns on the salamander flag.
    '-g' Groan. Turns on the groan flag.
    '-i' Igloo. Turs off Igloos.
    '-e' Encrypt. Does not actually encrypt anything.
    '-o' Optimize. Does not actually optimize anything.
    '-u' You don't know what you're getting!
    '-f' Accept a file as input.
    """
    print(out)

if sys.argv[1] == '-f':
    flag = '-f'
    file = sys.arg[2]
    print(f'Niiice. You entered a file named {file}, using the {flag} flag.')

if sys.argv[1] == '-s':
    flag = '-s'
    print(f'You turned on Salamanders using the {flag} flag!\n Sweet.')

if sys.argv[1] == '-g':
    var = 'g'
    print(f'GROANNNNNNNNN')

if sys.argv[1] == '-i':
    var = 'i'
    print(f'You turned off Igloos with the {i} flag! I agree. Too cold.')

if sys.argv[1] == '-e':
    print(f'You opted out of encryption. Good choice.')

if sys.argv[1] == '-o':
    print(f'You opted out of optimization. Perfect.')

if sys.argv[1] == '-u':
    print(f'BAM! Got you.')

#TODO: make something else