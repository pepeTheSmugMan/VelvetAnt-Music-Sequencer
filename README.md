# VelvetAnt Music Sequencer

VelvetAnt Music Sequencer **(VMS)** is an application made for creating musical compositions in style of chiptune/8-bit

## Setup (Linux)
    # Clone or download the project, then navigate to it's folder
    cd project_folder

    # Create virtual environment
    python3 -m venv src/.venv

    # Activate it
    source src/.venv/bin/activate

    # Install all dependencies
    python -m pip install -r requirements.txt

    # Run the project
    python src/main.py
---
    # to update requirements, use
    python -m pip freeze > requirements.txt

## Tech stack
Application is coded in Python and depends on libraries of
- Numpy, Scipy.Signal - for generating soundwaves
- SoundDevice - for communication with the sound card
