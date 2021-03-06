# gimpy
A simple image viewer that allows you to link class labels to image files for ML and AI purposes

### Project inception
While working on my PhD from home, I focussed mainly on image analysis and applying machine learning techniques. One particular project required me to annotate thousands of single cell images so that the file name contained the quantity of a certain feature in the cytoskeleton, which would then be easy to extract for training on these data. I devised a simple Python script for this purpose and only recently realised that other people may be facing the same issues.

It doesn't take too long to develop such a script, but I figured I can save people alot of development time if I can provide a readymade solution which can easily be installed in Python.

### How to use gimpy
Once installed, run `gimpy` in the terminal and a window will open up that requires you to input the class labels you want to insert into your file names just before the file extension. These settings can be saved and reloaded in JSON format, thus saving time when coming back to annotate more data, or to allow another user to annotate similar data in parallel using the same labels.

As you navigate through the images, press the number corresponding to your class label of choice and it will appear in the top right of the screen. This will also internally set it as the class label. Class labels are autosaved after every 20 images so no need to worry if the app crashes mid-annotation.

NOTE: once you click past the final image with the `<Right>` arrow key, the class labels will be saved to a json file and the viewer screen will be closed.

### Screens and bound key presses
##### Settings
* `s` save settings
* `l` load settings
* `a` start classifying images

##### Image viewer
* `<Left`   navigate left through images
* `<Right>` navigate right through images
* `1-8`     link image to class label bound to the specific number

##### Final
* `r` run again

##### File chooser dialogs
* `<Enter>` accept current selection (working on it)
* `<Esc>`   cancel and close the dialog
NOTE: Kivy App and Popup classes are bound by default to the `<Esc>` key

### Todo
- [ ] Add support for different file formats
- [ ] Fix double key press issue
- [ ] Add auto-reload method to viewer screen
- [X] Bind functions to keys
- [X] Convert layout to use Kivy for improved UI
- [X] Transfer save and load file data between popup and screen
- [X] Create setup.py to make app available as a package
- [X] Bind up and down arrow keys to navigate through z stacks
- [X] Bind left and right arrows to navigate through the image list
