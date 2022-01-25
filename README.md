## Linked ComboBoxes

#### Usage:
    
    Useful when you need to filter some other comboboxes based on selection text on
    some other combobox.
    
    Example: 
        comboxBox1 has selection "Tuhin".
        comboBox2 should show all places "Tuhin" has visited. (and hide the others)

### How to use?
To launch the UI
```bash
python main.py
```

### Additional modules required:
1. pandas
2. PyQt5

Note:
I have explicitly used 2 files, because, in the main implementation, that's how things were planned : )

<hr>

### Motivation
There were no convenient and simple ways to do this on stackoverflow or Qt Forum.
Also, using `QDataWidgetMapper` was making things over-complicated. Thus I implemented it
in a easier way.
