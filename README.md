# om-cc

This is om-cc for test

requires the following dependencies:

- htmlscript

### Installing Dependencies
to install htmlscript, we can use dnf:
```sh
dnf install htmlscript
```

### Running om-cc
you can run om-cc for debugging, with following command:
```sh
htmlscript -s 1020x600 -i /usr/share/icons/openmandriva.svg index.sh.htm 2> /dev/null;
```

##### translations
* inside the folder ```usr/share/om-cc/ ```
* there is a file called translation, all texts om-cc are it is from it that will 
* generate the translation files
* format it is as follows
```variavel=$"text that will be shown in om-cc"```

with the command
```sh
bash --dump-po-strings translation > om-cc.pot
```

om-cc.pot is the translation file.

htmlscript uses html, css and js to create the layout, if you want to make any changes or improvements
just edit the files with the format. sh.htm, and style.css that is inside the css folder.
files with the. scripts are run that will be read as if they were running through the terminal.

to execute a command within the html files (sh.htm) using the following command:
```sh
$(command to be executed)
```

example: 
```
     $(lsb_release -d | cut -d":" -f2) #shows the name of the Linux distribution
```      
