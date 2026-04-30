# RobotAI

RobotAI is an experimental voice-controlled robotics project that combines Python, Arduino, sockets, and local AI tools.

The current idea is to let the robot listen for a wake word, record a short voice command, send the audio to another computer for processing, generate a response, and deliver that response back to the Arduino so it can speak it aloud.

## Project goal

This project is being built as a prototype for a small robot assistant that can:

- detect a wake word with Edge Impulse
- record audio from a microphone
- send audio through a socket connection to another computer
- run Whisper locally on that computer for speech-to-text
- send the transcription to a local Ollama model on the same machine
- return the generated answer to the Arduino through the socket connection
- speak the final response back to the user
- control motors through Arduino-side functions

## Hardware

The project targets an **Arduino UNO Q**, a very recent Arduino board generation, used here as the hardware base for the robot control side.

## Current structure

- `python/programmaFinale.py` - main orchestration flow
- `python/ModelloEdge.py` - wake word detection with Edge Impulse
- `python/RegistrazionePyaudio.py` - microphone recording logic
- `python/richiesteModelli.py` - networking with Whisper and Ollama services
- `sketch/sketch.ino` - Arduino sketch for motor control and bridge-exposed functions

## Current flow

1. Wait for the wake word.
2. Record a short audio clip.
3. Send the audio to another computer through a socket connection.
4. Run Whisper locally on that computer to transcribe the audio.
5. Send the transcription to a local Ollama model on the same machine.
6. Return the generated response to the Arduino through the socket channel.
7. Let the Arduino play the final response by voice.

## Status

This repository is still a work in progress.

At the moment, it is closer to a functional prototype than a finished product. Some parts are already connected, while others are still being integrated and cleaned up.

## Python dependencies

Main Python packages currently used in the codebase:

- `requests`
- `PyAudio`
- `edge-impulse-linux`

You can install the basic Python dependencies with:

```bash
pip install -r requirements.txt
```

## Notes

- Some paths and IP addresses are currently hardcoded.
- The text-to-speech service runs on another computer in the current project design.
- Whisper is intended to run locally on the desktop machine that receives the audio.
- Ollama is also intended to run locally on that same desktop machine after transcription.
- The socket connection is the communication layer between the Arduino-side device and the desktop machine.
- Audio and Arduino integration depend on the target machine and board setup.
- The Arduino bridge utilities may require a board-specific runtime environment.

## Next improvements

- move configuration into a dedicated config file
- connect voice understanding directly to motor commands
- add better error handling
- clean up experimental scripts
- document board setup and deployment steps
