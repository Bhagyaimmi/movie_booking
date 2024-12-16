# Movie Booking System Backend

## **Overview**

This is a Django-based backend system designed to dynamically generate and manage movie booking slots for theaters. The system supports:

- Configurable weekly schedules.
- Weekly and custom unavailability settings.
- Dynamic generation of slots based on schedules and constraints.
- RESTful APIs for managing theaters, screens, and movie schedules.

## **Features**

1. **Dynamic Slot Generation**

   - Generates slots for movie screens based on theater schedules.
   - Accounts for weekly and custom unavailability.
   - Ensures slots do not overlap with unavailable periods.

2. **Configurable Weekly Schedules**

   - Allows theater owners to define opening and closing times for each day.
   - Includes the ability to mark weekly unavailability periods (e.g., maintenance hours).

3. **Custom Unavailability**

   - Allows marking of specific slots or entire dates as unavailable for a screen.

4. **RESTful API Endpoints**

   - Create and manage theaters, screens, and movies.
   - Configure availability and retrieve available slots.

---

## **Setup Instructions**

### **1. Clone the Repository**

```bash
$ git clone <repository_url>
$ cd movie-booking-system
```

### **2. Apply Migrations**

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

### **3. Run the Server**

```bash
$ python manage.py runserver
```

---

## **API Endpoints**

### **1. Create Theater**

**Endpoint:** `POST /api/theater/create/`

**Payload Example:**

```json
{
  "name": "C Theater 3",
  "location": "vizag"
}
```

**Response Example:**

```json
{
  "id": 3,
  "name": "C Theater 3",
  "location": "vizag"
}
```

---

### **3. Create Screen**

**Endpoint:** `POST /api/theater/create/`

**Payload Example:**

```json
{
  "theater": "3",
  "name": "screen3"
}
```

**Response Example:**

```json
{
  "id": 3,
  "name": "screen3",
  "theater": 3
}
```

---

### **4. Create Movie**

**Endpoint:** `POST /api/movie/create/`

**Payload Example:**

```json
{
  "title": "movie3",
  "duration": "300"
}
```

**Response Example:**

```json
{
  "id": 3,
  "title": "movie3",
  "duration": 300
}
```

---

### **5. Add Weekly Schedule and Unavailability**

**Endpoint:** `POST /api/theatre/3/availability/`

**Payload Example:**

```json
{
  "weekly_schedule": {
    "Wednesday": {"open": "08:00", "close": "22:00"},
    "Tuesday": {"open": "08:00", "close": "22:00"}
  },
  "weekly_unavailability": {
    "Sunday": [{"start": "14:00", "end": "16:00"}]
  }
}
```

**Response Example:**

```json
{
  "message": "Weekly schedule and unavailability configured successfully."
}
```

---

### **6. Add Custom Unavailability**

**Endpoint:** `POST /api/theatre/3/custom-unavailability/`

**Payload Example:**

```json
{
  "screen_id": 3,
  "unavailable_slots": [
    {"date": "2024-12-14", "start": "10:00", "end": "12:00"}
  ],
  "unavailable_dates": ["2024-12-23"]
}
```

**Response Example:**

```json
{
  "message": "Custom unavailability added successfully."
}
```

---

### **7. Fetch Available Slots**

**Endpoint:** `GET /api/theatre/1/slots/`

**Query Parameters:**

- `screen_id` (required)
- `start_date` (required)
- `end_date` (required)

**Example URL:**

```
GET /api/theatre/1/slots/?screen_id=1&start_date=2024-12-14&end_date=2024-12-20
```

**Response Example:**

```json
{
  "slots": [
    {
      "start_time": "08:00:00",
      "end_time": "10:00:00",
      "is_available": true
    },
    {
      "start_time": "10:00:00",
      "end_time": "12:00:00",
      "is_available": true
    },
    {
      "start_time": "12:00:00",
      "end_time": "14:00:00",
      "is_available": true
    },
    {
      "start_time": "14:00:00",
      "end_time": "16:00:00",
      "is_available": false
    },
    {
      "start_time": "16:00:00",
      "end_time": "18:00:00",
      "is_available": false
    },
    {
      "start_time": "18:00:00",
      "end_time": "20:00:00",
      "is_available": true
    },
    {
      "start_time": "20:00:00",
      "end_time": "22:00:00",
      "is_available": true
    }
  ]
}
```

---

## **Testing with Postman**

### **Steps:**

1. Import the Postman collection provided in the repository (if available).
2. Use the following endpoints for testing:
   - Create a theater: `POST /api/theater/create/`
   - Add weekly availability: `POST /api/theatre/{id}/availability/`
   - Add custom unavailability: `POST /api/theatre/{id}/custom-unavailability/`
   - Fetch slots: `GET /api/theatre/{id}/slots/`

### **Sample Inputs:**

Refer to the **Payload Examples** provided for each endpoint.

---

## **Swagger Documentation**

To access Swagger UI documentation, run the server and navigate to:

```
http://127.0.0.1:8000/api/swagger/
```

---

## **Code Quality and Practices**

- Modular design with separation of models, serializers, and views.
- Validation of inputs with meaningful error responses.
- Dynamic slot generation logic considering all constraints.

---

## **Submission**

1. Push your code to a public GitHub repository.
2. Add a demo video of the API endpoints working in the `README.md`.
3. Include instructions to generate the Swagger documentation in your repository.

---

## **Contact**

For questions or feedback, please contact [your email/contact info].

