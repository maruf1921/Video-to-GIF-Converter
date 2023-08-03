# Video to GIF Converter

Convert your favorite videos to GIF with this simple Python script using MoviePy library.

## Getting Started

### Prerequisites

Before running the script, make sure you have the following installed:

- Python 3.x
- moviepy library

You can install the moviepy library using pip:

```bash
pip install moviepy
```

### Usage

1. Clone the repository to your local machine or download the script directly.

2. Run the script `video_to_gif.py`.

3. The script will prompt you to select a video file. Click "Browse" and choose the video you want to convert.

4. After selecting the video, the script will process it and convert it to a GIF.

5. The output GIF will be saved in the same directory as the input video with the same name.

### Example

Here's an example of how to use the script:

```bash
python video_to_gif.py
```

Upon running the script, a file dialog will open. Select the video you want to convert, and the script will process it and save the GIF in the same directory.

## Note

- The GIF will be saved with a frame rate of 10 frames per second. You can modify the `fps` parameter in the script according to your preference.

- The script utilizes the `tkinter.filedialog` module to enable the selection of a video file via a file dialog. Therefore, ensure you have a graphical interface available or modify the script accordingly if you intend to run it on a headless server or through a command-line interface.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The script utilizes the MoviePy library, which can be found at [https://zulko.github.io/moviepy/](https://zulko.github.io/moviepy/).

Feel free to fork and modify the code to suit your needs. If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

Happy video to GIF converting! 🎬🚀
