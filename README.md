# Pet Management - Odoo Module 🐾

This Odoo module allows you to manage pets, their owners, species, weight tracking, and vaccination records. It is suitable for veterinary clinics, shelters, or any organization that needs to track animal health records.

## Features

* **Pet records** with:

  * Name
  * Date of birth
  * Owner
  * Species
  * Sex
  * Vaccination history
  * Weight tracking with date-specific entries
  * Per-pet weight evolution graph

* **Vaccination tracking**:

  * Vaccine name
  * Vaccination date
  * Veterinarian

* **Weight log**:

  * Daily weight entries
  * Line chart per pet (individual filtering)

* **Species management**:

  * Customizable list of species
  * Linked with pets

## Module Structure

```plaintext
pet_management/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── pets.py
│   ├── vaccinations.py
│   ├── species.py
│   └── weight_log.py
├── security/
│   └── ir.model.access.csv
├── views/
│   ├── views_pets.xml
│   ├── views_vaccinations.xml
│   ├── views_species.xml
│   └── views_weight_log.xml
└── README.md
```

## Installation

```bash
# Clone the module into your custom-addons directory
git clone https://github.com/riordi80/pet_management.git
```

1. Go to the Odoo interface
2. Activate Developer Mode
3. Go to **Apps** > **Update App List**
4. Search for `Pet Management` and install it

## Usage

* Go to **Pet Management > Ver Mascotas**
* Use the Odoo search bar to filter by pet name or owner
* Click any pet to view its form
* In the **Historial de peso** tab, register weight logs
* Click **Ver gráfico de peso** to view the pet's weight over time
* Use the **Vacunas** tab to register vaccines
* The **Species** field uses a reusable list (with creation from form)

## Requirements

* Odoo 18
* Docker (recommended)

## License

This module is released under the **MIT License**.

---

Created by **\[Richard Ortiz]**
