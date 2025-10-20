# 🖱️ Virtual Mouse - Hand Gesture Control

Control your computer mouse and screen brightness using hand gestures! This project uses computer vision and hand tracking to create a touchless interface for your computer.

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.5%2B-green)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Latest-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

- **Mouse Movement** - Move cursor with your index finger
- **Left Click** - Pinch index and middle fingers together
- **Right Click** - Pinch index, middle, and ring fingers together
- **Brightness Up** - Open all 5 fingers
- **Brightness Down** - Close all fingers (make a fist)
- **Smooth Tracking** - Built-in smoothening algorithm for stable cursor movement
- **Real-time FPS Display** - Monitor performance in real-time

## 🎥 Demo

*Add your demo GIF or video here*

```
Controls:
👆 Index finger up          → Move cursor
✌️  Index + Middle pinch    → Left Click
🤟 Index + Middle + Ring    → Right Click
✋ All 5 fingers open       → Increase Brightness
✊ Fist (all fingers closed) → Decrease Brightness
```

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- Webcam
- Windows/Linux/MacOS

### Step 1: Clone the repository

```bash
git clone https://github.com/yourusername/virtual-mouse.git
cd virtual-mouse
```

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the application

```bash
python VirtualMouse.py
```

## 📦 Dependencies

- OpenCV (`cv2`) - Computer vision and image processing
- MediaPipe - Hand tracking and landmark detection
- NumPy - Numerical computations
- AutoPy - Mouse control automation
- screen-brightness-control - Brightness adjustment

## 🎮 Usage

1. Run the script using `python VirtualMouse.py`
2. Position your hand in front of the webcam
3. Use the gestures mentioned above to control your mouse
4. Press 'q' to quit the application

### Tips for Better Performance

- Ensure good lighting conditions
- Keep your hand within the camera frame
- Maintain a distance of 1-2 feet from the camera
- Use a plain background for better hand detection

## 🛠️ Configuration

You can adjust these parameters in `VirtualMouse.py`:

```python
frameR = 0              # Frame reduction for better control
smoothening = 7         # Smoothening factor (higher = smoother but slower)
click_delay = 0.3       # Delay between clicks (in seconds)
brightness_delay = 0.2  # Delay between brightness changes
```

## 📁 Project Structure

```
virtual-mouse/
│
├── VirtualMouse.py          # Main application file
├── HandTracking.py          # Hand detection module
├── requirements.txt         # Project dependencies
├── README.md               # Project documentation
├── LICENSE                 # MIT License
└── .gitignore             # Git ignore file
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🐛 Known Issues

- Brightness control may not work on all operating systems
- Performance may vary based on lighting conditions
- Requires good lighting for accurate hand detection

## 📝 Future Improvements

- [ ] Add scroll gesture support
- [ ] Implement drag and drop functionality
- [ ] Add volume control gestures
- [ ] Multi-hand gesture support
- [ ] GUI for settings configuration
- [ ] Cross-platform brightness control

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👏 Acknowledgments

- [MediaPipe](https://mediapipe.dev/) for the amazing hand tracking solution
- [OpenCV](https://opencv.org/) for computer vision capabilities
- Inspired by touchless interface projects

## 📧 Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)

Project Link: [https://github.com/yourusername/virtual-mouse](https://github.com/yourusername/virtual-mouse)

---

⭐ If you found this project helpful, please consider giving it a star!

**Made with ❤️ and Python**
