//------------------------------------------------------------------------

aweControlPicker README.txt


– author			"Awesome" A.D.
– source			http://nyro.de/scripts/aweControlPicker.zip
– requires			Maya 2011 or higher
– version			1.0.4

//------------------------------------------------------------------------


/------ IMPORTANT NOTICE ------/

This readme has been deprecated in favor of an online documentation.
You can find the new documentation here:

http://nyro.de/scripts/aweControlPicker/



/------ INSTALLATION------/

Copy the script file (aweControlPicker.mel) to your scripts directory.
Under Windows, this is located under C:\User\Documents\maya\201x\scripts
You can determine your user directory from within Maya by executing the following MEL command:

internalVar -usd;

Copy the PNG images to your icons directory.
Again, under Windows, this is located under C:\User\Documents\maya\201x\prefs\icons
You can determine your icons directory by executing the following command:

internalVar -ubd;

After that is done restart Maya and execute the following command:

source "aweControlPicker.mel";

To start using the script, create a shelfbutton with the following command:

aweControlPicker;

Finally, I've supplied an image called aweControlPicker.png that you can use as an icon for your shelfbutton.

That's it!


