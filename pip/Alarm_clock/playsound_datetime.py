from pydub import AudioSegment
from pydub.playback import play
tone=AudioSegment.from_mp3("alarm.mp3")
play(tone)