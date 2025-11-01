# CycleGAN Style Transfer Application

A web-based application that allows users to upload images and apply artistic style transfer using CycleGAN models. Transform your photos into artworks inspired by famous painters like Monet, Van Gogh, and Picasso.

## Features

- **Image Upload**: Support for PNG, JPG, and JPEG formats
- **Multiple Artistic Styles**: Choose from Monet, Van Gogh, and Picasso styles
- **Real-time Processing**: Fast style transfer with GPU acceleration (if available)
- **User-friendly Interface**: Clean and intuitive web interface
- **Side-by-side Comparison**: View original and styled images together

## Technology Stack

- **Backend**: Flask (Python web framework)
- **Deep Learning**: PyTorch with CycleGAN architecture
- **Image Processing**: Pillow, torchvision
- **Frontend**: HTML5, CSS3, JavaScript

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/ashrithareddy04/ashritha.git
cd ashritha
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Use the application:
   - Click "Choose Image" to upload your photo
   - Select an artistic style (Monet, Van Gogh, or Picasso)
   - Click "Apply Style Transfer" to transform your image
   - View the results side-by-side with the original

## Architecture

### CycleGAN Model

The application uses a CycleGAN (Cycle-Consistent Generative Adversarial Network) architecture:

- **Generator**: ResNet-based generator with 9 residual blocks
- **Instance Normalization**: For style-agnostic feature learning
- **Reflection Padding**: To avoid artifacts at image borders

### Files Structure

```
ashritha/
├── app.py                 # Flask web application
├── cyclegan_model.py      # CycleGAN model architecture
├── style_transfer.py      # Style transfer processing logic
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Web interface
└── uploads/              # Temporary storage for images (auto-created)
```

## API Endpoints

- `GET /` - Main web interface
- `GET /styles` - Returns available artistic styles
- `POST /transfer` - Performs style transfer (requires image and style)
- `GET /result/<filename>` - Serves the styled image

## Configuration

The application can be configured through Flask app settings:

- `UPLOAD_FOLDER`: Directory for temporary file storage
- `MAX_CONTENT_LENGTH`: Maximum upload file size (default: 16MB)
- `ALLOWED_EXTENSIONS`: Supported image formats

## Notes

- The current implementation uses a randomly initialized model for demonstration purposes
- For production use, pre-trained CycleGAN weights should be downloaded and loaded
- GPU acceleration will be used automatically if CUDA is available

## Future Enhancements

- Add more artistic styles
- Implement model weight downloading from public repositories
- Add batch processing support
- Include style intensity control
- Add image history and favorites

## License

This project is open source and available under the MIT License.

## Acknowledgments

- CycleGAN paper: "Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks" by Zhu et al.
- PyTorch framework for deep learning implementation