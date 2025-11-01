# CycleGAN Style Transfer - Interface Overview

## Web Interface Layout

```
┌─────────────────────────────────────────────────────────────┐
│                  🎨 CycleGAN Style Transfer                  │
│        Transform your images with artistic styles of         │
│                    famous painters                           │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│                    [📁 Choose Image]                         │
│                  Selected: photo.jpg                         │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│                   Select Artistic Style                      │
│                                                              │
│         [Monet]    [Van Gogh]    [Picasso]                  │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│              [✨ Apply Style Transfer]                       │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│                         Results                              │
│                                                              │
│   ┌─────────────────┐        ┌─────────────────┐           │
│   │                 │        │                 │           │
│   │  Original Image │        │  Styled Image   │           │
│   │                 │        │                 │           │
│   └─────────────────┘        └─────────────────┘           │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Color Scheme

- **Primary Gradient**: Purple to Violet (#667eea → #764ba2)
- **Accent Colors**: Green for action button (#28a745)
- **Text**: Dark gray for readability (#333)
- **Background**: White cards on gradient background

## Features Visible in UI

1. **File Upload Section**
   - Visual button with emoji icon
   - File name display after selection
   - Accepts PNG, JPG, JPEG

2. **Style Selector**
   - Three clickable style buttons
   - Visual feedback on selection
   - Hover effects for better UX

3. **Transfer Button**
   - Disabled until both image and style selected
   - Loading spinner during processing
   - Clear success/error messages

4. **Results Display**
   - Side-by-side comparison
   - Original on left, styled on right
   - Full-size preview images
   - Rounded corners and shadows

## Responsive Design

- Desktop: Side-by-side layout
- Mobile: Stacked layout
- Adapts to screen size automatically

## User Flow

```
1. Open App → 2. Upload Image → 3. Select Style → 4. Apply → 5. View Results
      ↓              ↓                ↓               ↓            ↓
  Landing Page   File Dialog    Click Button     Processing   Side-by-Side
   Beautiful    PNG/JPG/JPEG   Monet/VanGogh/    Loading      Comparison
   Gradient        Only          Picasso         Spinner      Display
```

## API Endpoints Used by UI

1. **GET /** - Load main interface
2. **GET /styles** - Fetch available styles (populates buttons)
3. **POST /transfer** - Upload image and get styled result
4. **GET /result/<filename>** - Display styled image

## JavaScript Interactions

- Dynamic style button generation from API
- File selection with preview
- Form validation before submission
- Async image processing with loading state
- Error handling with user-friendly messages
- Success feedback with result display

## Accessibility Features

- Semantic HTML structure
- Clear button labels
- Visual feedback for all interactions
- Error messages in accessible format
- Keyboard navigation support

## Browser Compatibility

- Modern browsers (Chrome, Firefox, Safari, Edge)
- ES6 JavaScript features
- CSS Grid and Flexbox layouts
- Fetch API for requests
