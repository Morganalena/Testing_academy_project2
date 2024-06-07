# Testing Academy Project 2

## Description of Work

**Task:** Write three automated tests using the Playwright framework.

## Procedure

### 1. Selection of Website:
- Selected website: Google Maps.

### 2. Creation of Python File:
- Created a Python (.py) file with three automated tests for the selected website.

### 3. Simplify Test Writing:
- Imported the pytest-playwright plugin into the project to simplify writing the tests.

## Test Cases

### Functionality Testing on Google Maps:
1. **Search locations:** Validates the search functionality for given locations.
2. **Change map types:** Switches between different map types to verify the feature.
3. **Get directions:** Checks if directions can be obtained from a specified start point.

## Instructions to Run the Tests

### 1. Install Playwright and pytest-playwright plugin:
```
pip install playwright pytest-playwright
```

### 2. Install the required browser binaries:
```
playwright install
```

### 3. Run the tests:
```
pytest <your_test_file>.py
```
