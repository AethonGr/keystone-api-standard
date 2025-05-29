The `api` folder contains data models, endpoint definitions, and access scripts for querying and managing data. It is organized into subfolders, each focusing on a specific domain, such as transport operations, drivers, or vehicles. This modular structure ensures maintainability and extensibility.

## Subfolders

- **`entities/`**: Contains APIs, access scripts and logic for querying and managing data.
- **`data_model/`**: Defines the data models used throughout the API. These models provide a standardized structure and validation rules for entities such as drivers, vehicles, and transport operations.
- **`endpoints/`**: Contains endpoint definitions that map API paths to their corresponding functionalities, ensuring a clear and organized structure for handling requests.

## Files

- **`orchestrator_api.py`**: Serves as the central entry point for initializing and managing the APIs.

## Usage

1. **Navigate to the Relevant Subfolder**: Choose the subfolder based on the domain you want to manage (e.g., `driver`, `vehicle`, or `transport_operation`).
2. **Review the APIs**: Examine the APIs provided in the subfolder to understand their functionality.
3. **Implement Access Logic**: Modify the `_access.py` scripts in the `entities` subfolder to implement custom logic for querying and managing data.
4. **Link to Endpoints and Data Models**: Ensure that the access logic is properly linked to the endpoints in the `endpoints` folder and the data models in the `data_model` folder.

## Notes

- This folder provides an approach to managing data access logic, making it easier to maintain and extend the API.
- The modular design ensures that APIs across all domains follow a consistent structure, simplifying integration and customization.
