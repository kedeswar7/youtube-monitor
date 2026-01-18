from dotenv import load_dotenv
load_dotenv()

from youtube_service import CHANNEL_IDS, get_latest_video
from ai_service import analyze_video
from email_service import send_email
from youtube_transcript_api import YouTubeTranscriptApi

CUSTOM_PROMPTS = [
    "What is the video about?",
    "Key takeaways",
    "Who is this useful for?"
]

def main():
    for ch in CHANNEL_IDS:
        result = get_latest_video(ch)

        if not result:
            send_email(f"YouTube Report – {ch}", "No video uploaded from this channel.")
            continue

        video_id, title = result

        try:
            transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
            transcript = " ".join(t["text"] for t in transcript_data)

            responses = analyze_video(transcript, CUSTOM_PROMPTS)

            body = f"Video Title: {title}\n\n"
            for q, a in responses.items():
                body += f"{q}:\n{a}\n\n"

            send_email(f"YouTube Report – {ch}", body)

        except Exception:
            send_email(f"YouTube Report – {ch}", "Video uploaded but transcript not available.")

if __name__ == "__main__":
    main()