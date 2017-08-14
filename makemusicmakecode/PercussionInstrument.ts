
class PercussionInstrument {
    notes: String;
    pitch: number;
    length: number;
    beatMillis: number;
    // Maybe this needs changing?
    noteIndex: number;
    // milliseconds each beat takes
    repeat: boolean;

    constructor(notes: String, pitch: number, length: number, repeat?: boolean) {
        this.notes = notes;
        this.pitch = pitch;
        this.length = length;

        this.beatMillis = 1000;
        this.noteIndex = 0;
        this.repeat = repeat;
    }

    // Plays the next Percussion note
    public next(): void {
        if (this.hasNext()) {
            let note = this.notes.charAt(this.noteIndex);
            this.noteIndex = this.noteIndex + 1;
            if (note === "#") {
                music.playTone(this.pitch, this.length);
                music.rest(this.beatMillis - this.length);
                basic.showString("i");
            } else if (note === "-") {
                music.rest(this.beatMillis);
            } else {
                return;
           }
        } else {
            return;
        }
    }

    public hasNext(): boolean {
        return this.noteIndex < this.notes.length;
    }
}

// Example Usage with two instruments
// let snare = new PercussionInstrument("-#-#-##-", 400, 50);
// let kick = new PercussionInstrument("-#---#--", 100, 100);

// while (snare.hasNext() || kick.hasNext()) {
//     if (snare.hasNext()) {
//         snare.next();
//     }
//     if (kick.hasNext()) {
//         kick.next();
//     }
// }


