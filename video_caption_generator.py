import extract_audio
import transcribe_audio
import generate_subtitle_file
import add_subtitle_to_video
import convert_subtitle_file

"""
All the supported languages
LANGUAGES = [
    'Afrikaans', 'Albanian', 'Amharic', 'Arabic', 'Armenian', 'Azerbaijani',
    'Basque', 'Belarusian', 'Bengali', 'Bosnian', 'Bulgarian', 'Catalan',
    'Cebuano', 'Chichewa', 'Chinese (Simplified)', 'Chinese (Traditional)',
    'Corsican', 'Croatian', 'Czech', 'Danish', 'Dutch', 'English',
    'Esperanto', 'Estonian', 'Filipino', 'Finnish', 'French', 'Frisian',
    'Galician', 'Georgian', 'German', 'Greek', 'Gujarati', 'Haitian Creole',
    'Hausa', 'Hawaiian', 'Hebrew', 'Hebrew', 'Hindi', 'Hmong', 'Hungarian',
    'Icelandic', 'Igbo', 'Indonesian', 'Irish', 'Italian', 'Japanese',
    'Javanese', 'Kannada', 'Kazakh', 'Khmer', 'Korean', 'Kurdish (Kurmanji)',
    'Kyrgyz', 'Lao', 'Latin', 'Latvian', 'Lithuanian', 'Luxembourgish',
    'Macedonian', 'Malagasy', 'Malay', 'Malayalam', 'Maltese', 'Maori',
    'Marathi', 'Mongolian', 'Myanmar (Burmese)', 'Nepali', 'Norwegian',
    'Odia', 'Pashto', 'Persian', 'Polish', 'Portuguese', 'Punjabi', 'Romanian',
    'Russian', 'Samoan', 'Scots Gaelic', 'Serbian', 'Sesotho', 'Shona',
    'Sindhi', 'Sinhala', 'Slovak', 'Slovenian', 'Somali', 'Spanish',
    'Sundanese', 'Swahili', 'Swedish', 'Tajik', 'Tamil', 'Telugu', 'Thai',
    'Turkish', 'Ukrainian', 'Urdu', 'Uyghur', 'Uzbek', 'Vietnamese', 'Welsh',
    'Xhosa', 'Yiddish', 'Yoruba', 'Zulu',
]
"""

translate_language = 'Kannada'
input_video = "for_article.mp4"
input_video_name = input_video.replace(".mp4", "")

extracted_audio = extract_audio.extract_audio_from_video().extract_audio(input_video_name=input_video_name, input_video=input_video)

language, segments = transcribe_audio.transcribe_audio_class().transcribe(audio=extracted_audio)

subtitle_file = generate_subtitle_file.generate_sub_file_srt().generate_subtitle_file(language=language, segments=segments, input_video_name=input_video_name, translate_language=translate_language)

converted_subtitle_file = convert_subtitle_file.convert_srt_ass().convert_srt_to_ass(subtitle_file=subtitle_file)

add_subtitle_to_video.add_sub_to_video().add_subtitle_to_video(soft_subtitle=False, subtitle_file=converted_subtitle_file, input_video_name=input_video_name, input_video=input_video)
