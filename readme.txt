# 🚗 Vehicle Service Management System (CLI)

> A simple, console-based application to manage service records using Python. This project demonstrates core **CRUD** (Create, Read, Update, Delete) operations using an **in-memory dictionary data store**.

---

## ✨ Features

This system provides a menu-driven interface for basic service center operations:

* **Create (C):** Add a new service record for a customer's vehicle. Automatically generates a unique `SVCXXX` ID.
* **Read (R):** View a detailed list of all existing service records or search for a specific record by its ID.
* **Update (U):** Modify the owner, vehicle model, description, or update the service **Status** (e.g., Pending, In Progress, Completed).
* **Delete (D):** Remove an entire service record from the system.
* **Unique IDs:** Uses a sequential counter to generate simple, traceable Service IDs (e.g., `SVC001`).

---

## 🛠️ Technology Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Language** | Python 3.x | Core programming language. |
| **Data Structure** | Dictionary (In-Memory) | Stores service records temporarily. **Note: Data is lost upon program exit.** |
| **Interface** | Command-Line Interface (CLI) | User interaction is entirely console-based. |

---

## ⚙️ Installation and Setup

This project requires **Python 3** but has **no external dependencies** (no `pip install` required).

1.  **Clone the Repository (If on GitHub):**
    ```bash
    git clone [Your Repository URL Here]
    cd vehicle-service-crud-system
    ```
    *(If you are submitting locally, navigate to the folder containing your Python file.)*

2.  **Run the Application:**
    Execute the main Python script from your terminal:
    ```bash
    python main.py
    ```
    *(If your file is named `service_system.py`, replace `main.py` accordingly.)*

---

## 🚀 Usage Example

Once the program is running, the main menu will be displayed.