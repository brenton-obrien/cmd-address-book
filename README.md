# cmd-address-book
A simple python baseed command line address book program. This program is for me to practice object orientated programming and reading/writing to files.

Users can add new contacts which require a first name, last name, phone number and email address.
These details are used to create a 'Person Object'. These objects are then saved to a csv file so that they are persistant between sessions. The csv file is saved in the users public folder.

Users can then view all saved contacts in the address book which will print a list of names/details saved in the csv file.

Lastly users can delete contacts by searching their first name and last name. A temporary csv file is created which will only save contacts that dont match the search critera.
The original csv is then deleted and the temp csv replaces it.
