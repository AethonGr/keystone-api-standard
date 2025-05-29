The `test_server` folder contains sample server implementations that demonstrate how to expose APIs for transport operations, driver, and vehicle data. These implementations serve as a reference for developers to understand how the KEYSTONE API Standard can be utilized in real-world scenarios.

## Contents

The folder includes the following server samples:

- **`unified_server.py`**: A unified server that handles APIs for transport operations, vehicles, and drivers.
- **`transport_operation_server.py`**: A dedicated server for managing transport operation-related APIs.
- **`vehicle_server.py`**: A dedicated server for managing vehicle-related APIs.
- **`driver_server.py`**: A dedicated server for managing driver-related APIs.
- **`api_demonstration/`**: The main API folder containing implementation of the KEYSTONE API Standard, including endpoint handlers and the orchestrator API.
- **`data_samples/`**: Contains JSON files that simulate databases for demonstration purposes, providing sample data for transport operations, vehicles, and drivers.
- **`utils/`**: Contains utility modules which provide helper functions for interacting with JSON data storage.

Each server demonstrates how to initialize and expose the respective APIs using the KEYSTONE API Standard. While the provided implementations use the Flask framework, the APIs can be adapted to other frameworks as needed.

## Usage

To run a sample server, navigate to the parent directory of the `test_server` folder and execute the following command. For example, to run the unified server:

   ```bash
   python -m test_server.unified_server
   ```

Replace `unified_server` with the desired server file name (`transport_operation_server`, `vehicle_server`, or `driver_server`) to run a specific server.

By default, the server will be accessible at [http://127.0.0.1:5000](http://127.0.0.1:5000). The examples provided below assume this default address.

### Examples

The following API endpoints demonstrate how to interact with the APIs using the JSON files as simulated databases.

#### Vehicle Server

- **Get vehicle data by country code and plate number**:
  - Non-existent: [http://127.0.0.1:5000/vehicles/IT/AA0001/](http://127.0.0.1:5000/vehicles/IT/AA0001/)
  - Exists: [http://127.0.0.1:5000/vehicles/IT/AA1232/](http://127.0.0.1:5000/vehicles/IT/AA1232/)
  - Exists: [http://127.0.0.1:5000/vehicles/IT/BB4567/](http://127.0.0.1:5000/vehicles/IT/BB4567/)

- **Get insurance data by country code, plate number, and insurance ID**:
  - Non-existent: [http://127.0.0.1:5000/vehicles/IT/BB4567/insurances/987654320/](http://127.0.0.1:5000/vehicles/IT/BB4567/insurances/987654320/)
  - Exists: [http://127.0.0.1:5000/vehicles/IT/BB4567/insurances/987654321/](http://127.0.0.1:5000/vehicles/IT/BB4567/insurances/987654321/)
  - Exists: [http://127.0.0.1:5000/vehicles/IT/BB4567/insurances/987654322/](http://127.0.0.1:5000/vehicles/IT/BB4567/insurances/987654322/)

#### Driver Server

- **Get all driver data**:
  - Exists: [http://127.0.0.1:5000/drivers/](http://127.0.0.1:5000/drivers/)

- **Get tachograph card data by country code, VAT, and tachograph card ID**:
  - Non-existent: [http://127.0.0.1:5000/drivers/IT/IT0011228901/tachograph-cards/IT111111111/](http://127.0.0.1:5000/drivers/IT/IT0011228901/tachograph-cards/IT111111111/)
  - Exists: [http://127.0.0.1:5000/drivers/IT/IT0011228901/tachograph-cards/IT123423456/](http://127.0.0.1:5000/drivers/IT/IT0011228901/tachograph-cards/IT123423456/)

#### Transport Operation Server

- **Get all transport operation data**:
  - Exists: [http://127.0.0.1:5000/transport-operations/](http://127.0.0.1:5000/transport-operations/)

- **Get transport operation data by country code and plate number**:
  - Non-existent: [http://127.0.0.1:5000/transport-operations/IT/CC23227/](http://127.0.0.1:5000/transport-operations/IT/CC23227/)
  - Exists: [http://127.0.0.1:5000/transport-operations/IT/AA1232/](http://127.0.0.1:5000/transport-operations/IT/AA1232/)
  - Exists: [http://127.0.0.1:5000/transport-operations/IT/BB4567/](http://127.0.0.1:5000/transport-operations/IT/BB4567/)


## Features

- **Unified Server**: Combines APIs for transport operations, vehicles, and drivers into a single server for streamlined integration.
- **Dedicated Servers**: Provide focused implementations for specific domains.
- **Plug-and-Play Design**: Easily adapt the servers to your specific requirements by modifying the endpoint handlers or access logic.
- **Framework Flexibility**: While the examples use Flask, the APIs can be implemented in other frameworks (e.g., FastAPI, Django) to suit your project requirements.

## Notes 

- These servers are intended for demonstration and testing purposes only. The implementation is designed to help understand the KEYSTONE API Standard concepts quickly.
- The server samples use JSON files to simulate databases, providing a simplified data storage mechanism for demonstration.
- Each server implements query functionality to retrieve and return the respective data based on the APIs exposed in the Standard.
- The access and query logic is implemented in corresponding `_access.py` files, separating data access from API endpoint handling.
