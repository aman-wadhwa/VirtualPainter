==================================================================
 README - Virtual Painter Project
==================================================================

Project Title: Real-Time Virtual Painter using Hand Gesture Recognition

Description:
This Python application uses a webcam to track the user's hand gestures in real-time. It allows the user to draw on the screen with their index finger, select different colors, and use an eraser, all through intuitive hand movements.

Collaborators : Aman Wadhwa, Mansehaj Preet Singh
Roll no. : 102303550, 102303544

Work Division : 
- Aman Wadhwa : Backend vision engine
- Mansehaj Preet Singh : Frontend application logic
(Explained properly in the report)

------------------------------------------------------------------
Features:
- Real-time drawing using your index finger.
- Color palette selection (Purple, Blue, Green).
- Eraser tool functionality.
- Live visual feedback of hand tracking.

------------------------------------------------------------------
Dependencies / Requirements:
- Python 3.11 or Python 3.12 (64-bit version is required)
- OpenCV
- MediaPipe
- NumPy

------------------------------------------------------------------
Project Structure:
The project directory should contain the following files:

VirtualPainter/
├── requirements.txt
├── hand_detector.py
└── main.py

------------------------------------------------------------------
Dataset Information:
This project does not require any external datasets. It operates in real-time using the user's live webcam feed as its input source.

------------------------------------------------------------------
How to Run the Code:

1.  Prerequisite:
    Make sure you have a 64-bit version of Python 3.11 or 3.12 installed on your system.

2.  Download the Code:
    Place all the project files (`main.py`, `hand_detector.py`, `requirements.txt`) into a single folder named "VirtualPainter".

3.  Set up the Environment:
    Open a terminal or command prompt, navigate into your project folder, and install the Dependencies.

5.  Install Dependencies:
    Inside the folder,  run the following command to install all the necessary libraries:
    pip install -r requirements.txt

6.  Run the Application:
    Execute the main script to start the program:
    python main.py

------------------------------------------------------------------
How to Use the Application:

- To DRAW: Raise ONLY your index finger.
- To SELECT a color or the eraser: Raise BOTH your index and middle fingers and move your hand to the top of the screen to select a tool.
- To ERASE: First, select the eraser tool (the last option on the right, i.e. top right of screen). Then, switch back to drawing mode (only index finger up).
- To QUIT: Press the 'q' key on your keyboard.

(to select a tool, put both index and middle fingers up, to use that tool, keep only yhe index finger up)

==================================================================