# Student-result-data-management
# Number Analyzer Pro+ Backend

A fastAPI-based model for analyzing numbers and generating statistical reports. This backend provides endpoints to analyze numerical data, calculate statistics (mean, median, mode), and determine properties like prime numbers and perfect numbers.

## Features

- Number analysis (Even/Odd, Prime, Perfect, Positive/Negative)
- Statistical calculations (Mean, Median, Mode)
- Report generation and saving
- Download saved reports
- RESTful API endpoints
- CORS enabled for frontend integration

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/number-analyzer-backend.git
cd number-analyzer-backend
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

The server will start on `http://localhost:5000`

## API Endpoints

### 1. Health Check
**GET** `/health`

Check if the server is running.

**Response:**
```json
{
  "status": "healthy"
}
```

### 2. Analyze Numbers
**POST** `/analyze`

Analyze a list of numbers and get statistical results.

**Request Body:**
```json
{
  "numbers": [2, 3, 5, 6, 28]
}
```

**Response:**
```json
{
  "results": [
    {
      "Number": 2,
      "Even/Odd": "Even",
      "Prime": true,
      "Perfect": false,
      "Positive/Negative": "Positive"
    }
  ],
  "statistics": {
    "total": 5,
    "mean": 8.8,
    "median": 5.0,
    "modes": "2, 3, 5, 6, 28"
  }
}
```

### 3. Save Report
**POST** `/save-report`

Save analysis report to a file.

**Request Body:**
```json
{
  "results": [...],
  "statistics": {...},
  "filename": "my_report.txt"
}
```

**Response:**
```json
{
  "message": "Report saved successfully",
  "filepath": "reports/my_report.txt"
}
```

### 4. Download Report
**GET** `/download-report/<filename>`

Download a saved report file.

**Example:**
```
GET /download-report/my_report.txt
```

## Usage Examples

### Using curl
```bash
curl -X POST http://localhost:5000/analyze \
  -H "Content-Type: application/json" \
  -d '{"numbers": [2, 3, 5, 6, 28]}'
```

### Using Python requests
```python
import requests

response = requests.post('http://localhost:5000/analyze', 
                        json={"numbers": [2, 3, 5, 6, 28]})
print(response.json())
```

### Using JavaScript fetch
```javascript
fetch('http://localhost:5000/analyze', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    numbers: [2, 3, 5, 6, 28]
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

## Standalone CLI Usage

You can also run the statistical calculator as a standalone CLI application:

```bash
python statistical_calculator.py
```

Follow the prompts to enter numbers and generate reports interactively.

## Project Structure

```
number-analyzer-backend/
├── app.py                      # Flask backend application
├── statistical_calculator.py   # Core calculation logic
├── requirements.txt            # Python dependencies
├── .gitignore                 # Git ignore rules
├── README.md                  # Project documentation
└── reports/                   # Generated reports directory (auto-created)
```

## Configuration

The application runs in debug mode by default. For production deployment:

1. Set `debug=False` in `app.py`
2. Use a production WSGI server like Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## Network Access

- Local access: `http://127.0.0.1:5000`
- Network access: `http://YOUR_LOCAL_IP:5000` (shown in console output)

## Error Handling

The API returns appropriate HTTP status codes:
- `200` - Success
- `400` - Bad Request (invalid input)
- `404` - Not Found (endpoint or file doesn't exist)
- `500` - Internal Server Error

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Support

If you encounter any issues or have questions, please open an issue on GitHub.

