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

### Environment Variables

- `FLASK_DEBUG`: Set to `true` to enable debug mode (only for development, never in production)

## Security Features

The application implements several security measures:

- **Path Traversal Prevention**: Filenames are validated and sanitized
- **File Type Validation**: Only allowed image formats (PNG, JPG, JPEG) are accepted
- **File Size Limits**: Maximum upload size is enforced (16MB)
- **Debug Mode Control**: Debug mode is disabled by default for production safety
- **Error Handling**: Stack traces are not exposed to end users
- **Secure File Paths**: All file operations verify paths stay within intended directories

## Notes

- The current implementation uses a randomly initialized model for demonstration purposes
- For production use, pre-trained CycleGAN weights should be downloaded and loaded
- GPU acceleration will be used automatically if CUDA is available
- For production deployment, use a WSGI server like Gunicorn instead of Flask's development server

## Production Deployment

For production environments:

1. Set up a WSGI server:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

2. Use environment variables for configuration:
```bash
export FLASK_DEBUG=false
```

3. Set up proper logging and monitoring
4. Use HTTPS with SSL certificates
5. Implement rate limiting for API endpoints
6. Set up proper file cleanup for the uploads directory

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