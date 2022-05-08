# C15379616_Security_Assignment3

## This program is only about 50% done, it successfully connects to the Bitcoin network (if the network is working as it should be), sends a version message, receives the version response, sends a verack message, receives a verack response, and then receives inv messages and simply prints "Inv 1", "Inv 2" etc. This was done as there was not enough time to successfully parse the inv messages, create the getdata messages and request the information about the transactions. 

## To Run:
Simple clone the repo, open the file in Pycharm and click run. This was not set up to run as an individual script through command line (yet), it is simple a script that calls the main function at the bottom of the script. **Please Note** that this very frequently fails to run, I have no idea why but it only succeeds in running about 50% of the time. This is a problem that other students were also having. This is part of the reason that the program is so unfinished, I had wasted hours troubleshooting the program trying to understand why it was throwing errors, only for it to turn out to be the bitcoin network itself.
