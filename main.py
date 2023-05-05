from tkinter import Tk, Frame

import rtmidi

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()

if available_ports:
    midiout.open_port(0)
else:
    midiout.open_virtual_port("My virtual output")

class Config():
    def __init__(self):
        self.instrument = 0
        self.octave = 0
        self.sustain = False
        self.sustain_release = { }
        self.translate = {
                'q': 60, '2': 61, 'w': 62, '3': 63, 'e': 64,
                'r': 65, '5': 66, 't': 67, '6': 68, 'y': 69, '7': 70, 'u': 71,
                'i': 72, '9': 73, 'o': 74, '0': 75, 'p': 76,
                '[': 77, '=': 78, ']': 79, '\x08': 80, '\\': 81,

                'z': 48, 's': 49, 'x': 50, 'd': 51, 'c': 52,
                'v': 53, 'g': 54, 'b': 55, 'h': 56, 'n': 57, 'j': 58, 'm': 59,
                ',': 60, 'l': 61, '.': 62, ';': 63, '/': 64, '': 0, '\r': 0
            }
        self.state = { key : False for key in self.translate }

    def decrement_instrument(self):
        if self.instrument > 0: self.instrument = self.instrument - 1

    def increment_instrument(self):
        if self.instrument < 127: self.instrument = self.instrument + 1

    def decrease_octave(self):
        if self.octave > -3: self.octave = self.octave - 1

    def increase_octave(self):
        if self.ocave < 4: self.octave = self.octave + 1

config = Config()

def keyup(e):
    global config
    if e.char in [' ']:
        config.sustain = False
        for key in config.sustain_release:
            config.state[key] = False
            print(f"Key: {key}, State: False)")
            midiout.send_message(
                [ 0x90,
                  config.translate[key] + (config.octave * 12),
                  0
                  ]
                )
            config.sustain_release.clear()
    elif not config.sustain and e.char in config.state:
        config.state[e.char] = False
        midiout.send_message(
                [ 0x90,
                  config.translate[e.char] + (config.octave * 12),
                  0
                  ]
                )
    elif config.sustain:
        config.sustain_release[e.char] = False

def keydown(e):
    global config
    if e.char in config.state and not config.state[e.char]:
        config.state[e.char] = True
        if config.translate[e.char] > 0:
            midiout.send_message(
                [ 0x90,
                  config.translate[e.char] + (config.octave * 12),
                  96
                  ]
                )
    if e.char in ['<']:
        config.decrement_instrument()
        midiout.send_message([0xC0, config.instrument])

    if e.char in ['>']:
        config.increment_instrument()
        midiout.send_message([0xC0, config.instrument])

    if e.char in ['_']:
        config.decrease_octave()

    if e.char in ['+']:
        config.increase_octave()

    if e.char in [' ']:
        config.sustain = True

    if e.char in ['!']:
        root.destroy()

root = Tk()

frame = Frame(root, width=200, height=50)
frame.bind("<KeyPress>", keydown)
frame.bind("<KeyRelease>", keyup)
frame.pack()
frame.focus_set()

root.mainloop()

del midiout
