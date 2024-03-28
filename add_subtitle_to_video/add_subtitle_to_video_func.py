import ffmpeg

global input_video
class add_sub_to_video:
    def add_subtitle_to_video(self, soft_subtitle, subtitle_file, input_video, input_video_name):
        """
          Adds subtitles to the input video and creates an output video with the subtitles embedded.

          Parameters:
              soft_subtitle (bool): Indicates whether to add soft subtitles (True) or hard subtitles (False).
              subtitle_file (str): Path to the subtitle file.
              input_video (str): Path to the input video file.
              input_video_name (str): Name of the input video file.

          Executes:
              str: Path to the output video file with subtitles embedded.
          """

        input_video = input_video
        video_input_stream = ffmpeg.input(input_video)
        subtitle_input_stream = ffmpeg.input(subtitle_file)
        output_video = f"output-{input_video_name}-with-captions.mp4"
        subtitle_track_title = subtitle_file.replace(".srt", "")

        if soft_subtitle:
            stream = ffmpeg.output(
                video_input_stream, subtitle_input_stream, output_video, **{"c": "copy", "c:s": "mov_text"},
                **{"metadata:s:s:0": f"title={subtitle_track_title}"}
            )
            ffmpeg.run(stream, overwrite_output=True)
        else:
            stream = ffmpeg.output(video_input_stream, output_video, vf=f"ass={subtitle_file}")

            ffmpeg.run(stream, overwrite_output=True)
