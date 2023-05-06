# winpyano
Lightweight Python recreation of MS Windows "Piano" (by Gregor Brecko).

## About
A simple piano application recreated in a modern language. Greatly inspired by Gregor's Piano 
application for MS-DOS, colloquially known to me as "WinPiano". It follows the same key layout 
and doesn't have a GUI (to make it lighter) but added new features such as sustaining notes and 
moved the octave switching, instrument changing and quitting functions to keyboard actions.

### Implementation
Uses Tkinter to handle key presses. Uses rtmidi to send signals to your local MIDI driver.

## Getting Started
To get a local copy up and running follow these simple example steps.

### Prerequisites
* Python 3.7+
* [python-rtmidi](https://github.com/SpotlightKid/python-rtmidi)

### Installation
* Download main.py from this repo.

## Usage
* Open main.py (create virtual environments if you prefer)
* There are two sets of keys on your keyboard. (add illustration here),
press any of these keys to play a corresponding note
* Hold the Spacebar (' ') to sustain keys
* Pressing - or + will shift (decrease and increase, respectively) the current octave
* Pressing < or > will change (decrease and increase, respectively) the current instrument
* Pressing Shift + 1 ('!') will exit

## Roadmap
* Initial MVP - X
* Code Cleanup
* GUI extention to actually recreate the old UI? (might as well, not yet sure on shareware licenses) 
* Recording and replaying (export and import MIDI or some custom file type)
* This allows for demo playbacks

## License
Licensed under GPL-3.0.

## Contact

## Acknowledgements

