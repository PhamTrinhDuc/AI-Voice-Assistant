import asyncio
from dotenv import load_dotenv
from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli, llm
from livekit.agents.voice_assistant import VoiceAssistant
from livekit.plugins import openai, silero



load_dotenv()

async def entrypoint(ctx: JobContext):
    inital_ctx = llm.ChatContext().append(
        role="system",
        text=(
            "You are a voice assistant created by LiveKit. Your interface with users will be voice. "
            "You should use short and concise responses, and avoiding usage of unpronouncable punctuation."
        )
    )

    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)
    assitant = VoiceAssistant(
        vad=silero.VAD.load(), # phát hiện xem người dùng có nói hay không 
        stt=openai.STT(),
        llm=openai.LLM(),
        tts=openai.TTS(),
        chat_ctx=inital_ctx
    )
    assitant.start(ctx.room)

    await asyncio.sleep(1)
    await assitant.say("Hello, I am a voice assistant created by LiveKit. How can I help you today?", allow_interruptions=True)


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))