import subprocess
import random,os


class convert_srt_ass:
    def convert_srt_to_ass(self, subtitle_file):
        """
        Convert .srt to .ass type.

        Parameters:
            subtitle_file (str): The name of the subtitle file.

        Returns:
            str: Output .ass type file.
        """
        out = (subtitle_file.split('.')[0] + str(random.randint(1000, 1000000))) + ".srt"

        output_file = out.replace(".srt", ".ass")
        command = [
            "ffmpeg",
            "-i", subtitle_file,
            "-vf", "ass=subtitle.ass",
            output_file
        ]

        subprocess.call(command)
        return output_file
