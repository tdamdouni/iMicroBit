import {Sequence} from "./Sequence";

export class Percussion {
    pitch: number;
    length: number;
    sequence: Sequence;
    beatMillis: number;
    constructor(pattern: string, pitch: number, length: number) {
        this.pitch = pitch;
        this.length = length;
        this.beatMillis = 1000;

        let callback = () => {
            music.playTone(this.pitch, this.length);
            music.rest(this.beatMillis - this.length);
        }

        this.sequence = new Sequence(pattern, callback);
    }

    public playNext(): boolean {
        return this.sequence.next();
    }

    public isPlayingNextBeat(): boolean {
        return this.sequence.isNextOn();
    }
}