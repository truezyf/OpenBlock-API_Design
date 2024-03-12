# OpenBlock-API_Design

The Open Block Labs API provides access to a dataset containing information about wallet transactions. This REST API allows clients to query point values accumulated by wallet addresses over specified date ranges.

## Getting Started

### Prerequisites

- Python 3.8+
- Flask
- Flask-JWT-Extended
- Pandas

### Installation

1.Clone the repository and navigate to the project directory:

```bash
git clone git@github.com:truezyf/OpenBlock-API_Design.git
cd OpenBlock-API_Design
sh init.sh
```
2.Install the required dependencies:

```bash
pip install flask flask-jwt-extended pandas
```

### Running the API

Launch the Flask server by executing:
```bash
python src/main.py
```
The server will start, and the API will be accessible at `http://localhost:5000`.

## API Endpoints
### Authentication

### Login

- **POST** `/login`
- **Purpose**: Authenticates users and provides a JWT for accessing protected endpoints.
- **Request Body**:

```json
{
  "username": "admin",
  "password": "password"
}
```
- **Response**:
  - **Success**: `200 OK` with JWT
  - **Failure**: `401 Unauthorized`

### Points Query

Get Points

- **GET** `/points`
- **Headers**: `Authorization: Bearer <ACCESS_TOKEN>`
- **Query Parameters**:
  - `wallet_address` - The wallet address to query.
  - `from_date` - The start date for the query range (YYYY-MM-DD).
  - `to_date` - The end date for the query range (YYYY-MM-DD).

#### Response

- **Success**: `200 OK` with wallet address, date range, and total points.
- **Failure**: `400 Bad Request` if parameters are missing or incorrect.

## Client Example Code

- **client.py** is under the example folder

