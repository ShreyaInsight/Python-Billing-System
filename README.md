# 🧾 Billing System in Python (Electronic Store)

![final](https://cdn.discordapp.com/attachments/1265222639568425010/1361308844034359408/1214u238ury092o3u8f03.png?ex=67fe4928&is=67fcf7a8&hm=ab15b481683d6751489c7b585a3301bc489394e2273666c89d50187245382326&)
A Python-based billing system for an electronic store offering electronic devices like phones, laptops, and HDDs. This project utilizes Python fundamentals including loops, exception handling, file read/write operations, and modular design to create a complete CLI billing solution.

---

## 📌 Overview

This project simulates a real-world billing system for an electronic store. The system allows customers to choose products (with interactive selection via the keyboard), calculates the purchase amount (including discount logic), updates the stock, and generates a unique invoice file for each transaction.

---

## 🎯 Key Features

- **Interactive Product Selection:**  
  Choose products using arrow keys (via a CLI library) for a modern, user-friendly experience.

- **Dynamic Billing and Discounts:**  
  Compute item totals and apply discounts based on overall purchase amounts.

- **Inventory Management:**  
  Reads product information from a file (`products.txt`), updates stock after purchases, and writes changes back to the file.

- **Invoice Generation:**  
  Creates uniquely named invoice files (timestamp-based) with detailed billing information.

- **Modular Codebase:**  
  Organized into separate Python modules (`read.py`, `purchase.py`, and `write.py`) for maintainability.

---

## 🛠️ Technologies and Dependencies

- **Python 3.x**

- **Standard Libraries:**  
  `datetime`, `os`, `sys`

- **Optional CLI Library for Enhanced Selection:**  
  Use `questionary` or `InquirerPy` to enable arrow key navigation in the terminal.  
  To install `questionary`, run:

  ```bash
  pip install questionary

## 📁 Project Structure

```
Billing-System-In-Python/
│
├── main.py               # Entry point for the system
├── read.py               # Module to read product data
├── purchase.py           # Main logic for purchase flow
├── write.py              # Updates inventory after purchase
├── products.txt          # Text file storing product inventory
├── <invoice>.txt         # Invoices generated dynamically
└── README.md             # Project documentation
```
