# CycleGAN Style Transfer - Quick Start Guide

## What is Style Transfer?

Style transfer is a technique in computer vision that applies the artistic style of one image to the content of another. Using CycleGAN (Cycle-Consistent Generative Adversarial Networks), this application can transform your photographs into artworks that mimic the styles of famous painters.

## Available Styles

### 1. Monet
Transform your photos to look like impressionist paintings by Claude Monet, featuring:
- Soft brushstrokes
- Light and color emphasis
- Dreamy, atmospheric quality

### 2. Van Gogh
Apply Vincent van Gogh's post-impressionist style with:
- Bold, swirling brushstrokes
- Vibrant, expressive colors
- Emotional intensity

### 3. Picasso
Create cubist-inspired artwork in Pablo Picasso's style with:
- Geometric shapes
- Abstract forms
- Multiple perspectives

## How to Use

### Step 1: Prepare Your Image
- Use a high-quality photo (PNG, JPG, or JPEG)
- Recommended size: at least 512x512 pixels
- Maximum file size: 16MB

### Step 2: Upload
1. Click the "Choose Image" button
2. Select your image from your computer
3. The original image will appear in the preview

### Step 3: Select Style
1. Choose one of the three artistic styles:
   - Monet
   - Van Gogh
   - Picasso
2. The selected style will be highlighted

### Step 4: Transform
1. Click "Apply Style Transfer"
2. Wait for processing (typically 5-30 seconds)
3. View your transformed image alongside the original

## Tips for Best Results

1. **Subject Matter**: The style transfer works best on:
   - Landscapes
   - Portraits
   - Architecture
   - Nature scenes

2. **Image Quality**: Use clear, well-lit photos for better results

3. **Resolution**: Higher resolution images produce more detailed results but take longer to process

4. **Experiment**: Try the same image with different styles to see which works best

## Technical Details

### Processing Pipeline

1. **Upload**: Image is uploaded to the server
2. **Preprocessing**:
   - Image is resized to 256x256 pixels
   - Converted to tensor format
   - Normalized for neural network input
3. **Style Transfer**: CycleGAN generator applies the selected style
4. **Postprocessing**:
   - Denormalization
   - Tensor to image conversion
   - Format conversion for web display
5. **Display**: Styled image is shown alongside original

### Performance

- **CPU Processing**: 10-30 seconds per image
- **GPU Processing**: 2-5 seconds per image
- **Memory Usage**: ~2GB for model + processing

## Troubleshooting

### "Invalid file type" Error
- Ensure your file is PNG, JPG, or JPEG format
- Check that the file has a proper extension

### "File too large" Error
- Reduce image file size below 16MB
- Use image compression tools

### Processing Takes Too Long
- Wait up to 60 seconds for CPU processing
- Try a smaller image
- Restart the application if it seems stuck

### Styled Image Looks Strange
- Try a different style
- Use a higher quality source image
- Ensure adequate lighting in the original photo

## Examples

Here are some example use cases:

1. **Vacation Photos**: Transform your travel photos into museum-worthy artwork
2. **Portraits**: Give family photos an artistic makeover
3. **Nature Photography**: Turn landscape shots into impressionist masterpieces
4. **Creative Projects**: Generate unique art for presentations or social media

## API Usage

For programmatic access, you can use the REST API:

```bash
# Get available styles
curl http://localhost:5000/styles

# Upload and transform an image
curl -X POST http://localhost:5000/transfer \
  -F "image=@photo.jpg" \
  -F "style=monet"

# Response will include output_image filename
# Download the result
curl http://localhost:5000/result/styled_<filename>.jpg -o result.jpg
```

## Privacy and Data

- Uploaded images are temporarily stored during processing
- Images are automatically cleaned up after processing
- No images are permanently stored or shared
- All processing happens on the server

## Support

If you encounter issues or have questions:
1. Check the troubleshooting section above
2. Review the main README.md for technical details
3. Check application logs for error messages
4. Open an issue on GitHub

## Credits

This application uses:
- CycleGAN architecture from "Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks"
- PyTorch deep learning framework
- Flask web framework
