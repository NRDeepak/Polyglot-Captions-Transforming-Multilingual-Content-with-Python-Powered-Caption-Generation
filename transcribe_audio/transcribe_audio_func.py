from faster_whisper import WhisperModel


class transcribe_audio_class:
    def transcribe(self, audio):
        """
        Transcribing the audio file extracted from the input video.

        Parameters:
            audio (str): The name of the extracted audio file.

        Returns:
            tuple: A tuple containing the detected language and the segments of the transcription.
               - language (str): The language of the transcription.
               - segments (list): A list of Segment objects containing the transcribed segments.
        """

        model = WhisperModel("small")
        segments, info = model.transcribe(audio)
        language = info[0]
        print("Transcription language", info[0])
        segments = list(segments)
        for segment in segments:
            # print(segment)
            print("[%.2fs -> %.2fs] %s" %
                  (segment.start, segment.end, segment.text))
        return language, segments
