import format_time
import translate_text
import check_for_language

format_time_obj = format_time.format_time_class()
check_language_obj = check_for_language.check_language()

class generate_sub_file_srt:



    def generate_subtitle_file(self, language, segments, input_video_name, translate_language):
        """
            Generate a subtitle file and translate it to the user's selected language..

            Parameters:
                language (str): Language of the audio file.
                segments (str): A list of Segment objects containing the transcribed segments.
                input_video_name (str): The name of the input video file.
                translate_language (str): Language specified by user to translate the subtitle.

            Returns:
                str: Output subtitle file.
            """
        translation_lang_keyword = check_language_obj.check_lang_if_exists(translate_language=translate_language)
        subtitle_file = f"sub-{input_video_name}.{language}.srt"
        text = ""
        for index, segment in enumerate(segments):
            segment_start = format_time_obj.format_time(seconds=segment.start)
            segment_end = format_time_obj.format_time(seconds=segment.end)
            text += f"{str(index + 1)} \n"
            text += f"{segment_start} --> {segment_end} \n"
            translated_text = translate_text.translate_text_class().translate_text(segment.text, translation_lang_keyword)
            text += f"{translated_text} \n"
            text += "\n"


        with open(subtitle_file, "w", encoding="utf-8") as f:
            f.write(text)
        f.close()

        return subtitle_file
