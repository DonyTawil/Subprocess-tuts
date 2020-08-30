# File to learn the capabilities of subprocess
# From https://stackoverflow.com/questions/163542/how-do-i-pass-a-string-into-subprocess-popen-using-the-stdin-argument


from subprocess import Popen, PIPE, STDOUT

#p = Popen(['echo', "yo"], stdout=PIPE, stdin=PIPE, stderr=STDOUT) # By passing STDOUT to stderr I combine stdout
#echo_stdout = p.communicate(input=b'Hello word')                  # And stderr into one stream, We pass PIPE to be able 
                                                                  # to pass and receive data using communicate

#print(echo_stdout[0].decode())                                   # Was not able to get p to echo hello world
#echo_stdout2 = p.communicate(input=b'Whatup')                    # This did not work for some reason, cannot send two commands with "echo"
                                                            
                                                            
p = Popen(['grep', 'f'], stdout=PIPE, stdin=PIPE, stderr = STDOUT)
grep_stdout = p.communicate(input=b'one\ntwo\nthree\nfour\nfive\nsix')[0]
print(grep_stdout.decode())                                                          

grep_stdout = p.communicate(input=b'for the love of KNOWLEDGE')    # This doesn't work
print(grep_stdout.decode())                                        # According to this https://stackoverflow.com/questions/28616018/multiple-inputs-and-outputs-in-python-subprocess-communicate
                                                                   # It doesn work because p would have already closed by now 
