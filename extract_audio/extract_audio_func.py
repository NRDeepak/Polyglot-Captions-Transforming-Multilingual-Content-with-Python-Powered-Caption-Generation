import ffmpeg

class extract_audio_from_video:


    def extract_audio(self, input_video_name, input_video):
        """
            Extracts audio ({file_name}.wav) from the input video file.

            Parameters:
                input_video_name (str): The name of the input video file.
                input_video (str): The path to the input video file.

            Returns:
                str: The path to the extracted audio file.
            """


        extracted_audio = f"audio-{input_video_name}.wav"
        stream = ffmpeg.input(input_video)
        stream = ffmpeg.output(stream, extracted_audio)
        ffmpeg.run(stream, overwrite_output=True)
        return extracted_audio
