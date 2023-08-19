import yt_dlp
import requests

def get_subs(video_url):
    ydl_opts = {
        'skip_download': True,
        'writesubtitles': True,
        'allsubtitles': True,
    }

    subtitles = []

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        video_info = ydl.extract_info(video_url, download=False)
        if 'requested_subtitles' in video_info:
            for lang, sub in video_info['requested_subtitles'].items():
                sub_url = sub['url']
                sub_data = requests.get(sub_url).text
                subtitles.append({
                    'language': lang,
                    'data': sub_data,
                })

    return subtitles

if __name__ == "__main__":
    video_id = 'nm1TxQj9IsQ&t'
    subtitles = get_subs(f'https://www.youtube.com/watch?v={video_id}')
    print(subtitles)
