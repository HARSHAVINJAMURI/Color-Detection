# Color Detection in Images 🖼️🎨

This Python application allows users to upload an image, detect the colors at specific points by double-clicking, and get the color name along with its RGB values.

---

## Features ✨

- **File Upload**: Select any image file (`.jpg`, `.jpeg`, `.png`) via a graphical file chooser.
- **Color Identification**: Double-click on any area in the image to get the closest color name and its RGB values.
- **Interactive UI**: The application dynamically updates the image with a color overlay and text display.
- **Supports Light and Dark Colors**: Text is automatically adjusted for better visibility based on the background.

---

## Demo 📸

1. **Upload an Image**: Use the file dialog to upload an image.
2. **Identify Colors**: Double-click anywhere on the image to display the detected color name and RGB values.
3. **Output Example**:

   - **Uploaded Image**:
     ![Uploaded Image Example](https://via.placeholder.com/800x400.png?text=Uploaded+Image)

   - **Color Detection in Action**:
     ![Color Detection Example](https://via.placeholder.com/800x400.png?text=Color+Detection+Output)

---

## Installation & Setup ⚙️

Follow the steps below to run this application on your local system.

### Prerequisites

Ensure you have the following installed:

- **Python 3.8+**
- Python libraries: `opencv-python`, `pandas`, `numpy`, `tkinter`

You can install the dependencies using the command:

```bash
pip install opencv-python pandas numpy
```
## Clone the Repository
- Clone the repository to your local system:
```bash
git clone https://github.com/your-username/color-detection.git
cd color-detection
```
## Add the Required Files
**colors.csv**: Ensure colors.csv is placed in the root directory of the project.
This file should contain color information in the format:
- color,color_name,hex,R,G,B
- Red,Red,#FF0000,255,0,0
- Green,Green,#00FF00,0,255,0
- Blue,Blue,#0000FF,0,0,255
...

You can find a sample colors.csv file online or generate your own.

## How to Run 🏃‍♂️
Navigate to the project directory:
```
cd color-detection
```
Run the application:
```
python color_detection.py
```
## Follow the instructions:

- A file dialog will appear. Select the image you want to analyze.
- Double-click on any part of the image to identify the color.
## Exit the application:
- Press Esc or close the window to exit.
## Usage Example 💡
**Input**: A sample image.
- **Action**: Double-click on the image to detect colors.
- **Output**: The color name and its RGB values are displayed on the image in real time.

## Technical Stack 🛠️
- **Python**: Core programming language.
- **OpenCV**: For image processing and UI interaction.
- **Pandas**: For reading and processing the color data from colors.csv.
- **Numpy**: For numerical computations.
- **Tkinter**: For the file upload dialog.
## File Structure 📂
color-detection/  
│  
├── color_detection.py    # Main Python script  
├── colors.csv            # CSV file containing color data  
├── README.md             # Project documentation  
└── requirements.txt      # Dependencies for the project  
## Additional Features to Add 📌
If you're looking to enhance this project, consider adding:

- **Real-time Camera Input**: Use a webcam to detect colors in real-time.
- **Output Logging**: Save detected colors and their RGB values to a file.
- **Image Filters**: Add functionality to filter specific colors in the image.
##  License 📜
- This project is licensed under the MIT License.

## Contributions 🤝
- Contributions, issues, and feature requests are welcome! Feel free to check the issues page or submit a pull request.

## Author 👤  
Harsha  
- GitHub: HARSHAVINJAMURI
- Email: Vinjamuriharsha123@gamil.com
