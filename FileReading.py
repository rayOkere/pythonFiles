file = open("git_commands.txt","r")
print(file.readlines()[2:])
file.close()
'''open is a function that opens a file in the folder it's in. The first parameter is the name of the file 
and the second parameter is what you want to do with the file after opening it. In this case, the second
parameter is r. What this means is the file is being opened for reading purposes. This means the only 
thing you can do with this file after opening it is read it.'''
'''print(file.readlines()[2:]) - what this does is print out part of the file. The parts of the file that
are printed out can be set using () and []. In this case, there is nothing in () and 2: in []. What this
does is print out the entire file apart from 2(indexing starts at 0 so this would be the third line)'''