# gimpy
A simple image viewer that allows you to rename image files for ML and AI purposes

### Project inception
While working from home, I focussed more on image analysis and applyig machine learning techniques to the data. One particular project required me to annotate thousands of single cell images so that the file name contained the quantity of a certain feature in the cytoskeleton, which would then be easy to extract for training on these data. I devised a simple Python script for this purpose and only recently realised that other people may be facing the same issues.

It doesn't take too long to develop such a script, but I figured I can save alot of development time if I can provide a readymade solution which can easily be installed in Python.

### How to use gimpy
Once installed, run `gimpy` in the terminal and a window will open up that requires you to input the class labels you want to insert into your file names just before the file extension. These settings can be saved and reloaded, thus saving some time when coming back to annotate more data or to allow someone else to annotate similar data in parallel using the same labels.

### Todo
- [ ] Convert layout to use Kivy for improved UI
- [X] Bind up and down arrow keys to navigate through z stacks
- [ ] Bind left and right arrows to navigate through the image list