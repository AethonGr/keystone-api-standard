"""
This module provides a utility class for entity access classes to interact with JSON data storage.
The JsonAccessManager handles reading from and writing to JSON files for persistent data storage
across different entity access modules.
"""

import json
import logging
import os
from typing import Any, Dict, List, Optional


class JsonAccessManager:
    """
    A utility class to handle JSON file operations for entity access classes.
    """

    def __init__(self, filepath: str):
        """
        Initialize the JSON access manager.

        Args:
            filepath: Path to the JSON file
        """
        self.filepath = filepath
        self.logger = logging.getLogger(__name__)

        # Check if file exists and log its absolute path for debugging
        if os.path.exists(self.filepath):
            self.logger.info(f"JSON file found at: {os.path.abspath(self.filepath)}")
        else:
            self.logger.error(
                f"JSON file NOT found at: {os.path.abspath(self.filepath)}"
            )

    def load_data(self) -> List[Dict[str, Any]]:
        """
        Load all data from the JSON file.

        Returns:
            List of data items as dictionaries
        """
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.logger.info(
                    f"Successfully loaded {len(data)} records from {self.filepath}"
                )
                return data
        except json.JSONDecodeError as e:
            self.logger.error(f"Error decoding JSON from {self.filepath}: {str(e)}")
            return []
        except FileNotFoundError as e:
            self.logger.error(f"File not found: {self.filepath}: {str(e)}")
            return []
        except Exception as e:
            self.logger.error(f"Unexpected error loading data: {str(e)}")
            return []

    def get_all(self) -> List[Dict[str, Any]]:
        """
        Get all records from the JSON file.

        Returns:
            List of all records
        """
        return self.load_data()

    def get_by_multiple_fields(self, **field_values) -> List[Dict[str, Any]]:
        """
        Get records matching multiple field values.

        Args:
            **field_values: Field names and values to match

        Returns:
            List of matching records
        """
        data = self.load_data()
        result = []

        for item in data:
            match = True
            for field_name, field_value in field_values.items():
                if item.get(field_name) != field_value:
                    match = False
                    break
            if match:
                result.append(item)

        return result

    def get_nested_field(
        self, parent_identifiers: Dict[str, Any], nested_field: str
    ) -> Optional[Any]:
        """
        Get a nested field from a record identified by parent identifiers.

        Args:
            parent_identifiers: Dictionary of field names and values to identify the parent record
            nested_field: Name of the nested field to retrieve

        Returns:
            The nested field value if found, None otherwise
        """
        records = self.get_by_multiple_fields(**parent_identifiers)
        if not records:
            return None

        record = records[0]  # Take the first matching record
        return record.get(nested_field)

    def get_nested_array_items(
        self, parent_identifiers: Dict[str, Any], array_field: str
    ) -> List[Dict[str, Any]]:
        """
        Get all items from a nested array field in a record.

        Args:
            parent_identifiers: Dictionary of field names and values to identify the parent record
            array_field: Name of the nested array field

        Returns:
            List of items in the nested array
        """
        nested_field = self.get_nested_field(parent_identifiers, array_field)
        if not nested_field or not isinstance(nested_field, list):
            return []

        return nested_field

    def get_nested_array_item_by_id(
        self, parent_identifiers: Dict[str, Any], array_field: str, item_id: Any
    ) -> Optional[Dict[str, Any]]:
        """
        Get a specific item from a nested array field by its ID.

        Args:
            parent_identifiers: Dictionary of field names and values to identify the parent record
            array_field: Name of the nested array field
            item_id: ID value to search for in the array items

        Returns:
            The matching item if found, None otherwise
        """
        array_items = self.get_nested_array_items(parent_identifiers, array_field)
        for item in array_items:
            if item.get("id") == item_id:
                return item

        return None

    def find_by_nested_field_value(self, *args, **kwargs) -> List[Dict[str, Any]]:
        """
        Find records where nested fields match specific values.

        This method can be called in several ways:
        1. With a dot notation path and a value: find_by_nested_field_value("vehicle.plateNumber", "AA1232")
        2. With multiple field-value pairs: find_by_nested_field_value(countryCode="IT", plateNumber="AA1232")
        3. With a combination of both: find_by_nested_field_value("vehicle.type", "Truck", driver_id=123456789)

        Args:
            *args: Optional positional arguments for path and value
            **kwargs: Field-value pairs to match at the top level or using dot notation keys

        Returns:
            List of matching records
        """
        data = self.load_data()
        results = []

        # Case 1: Using dot notation path and value
        if len(args) == 2:
            path, value = args
            path_parts = path.split(".")

            for record in data:
                if self._check_nested_path(record, path_parts, value):
                    match = True

                    # Also check any additional kwargs
                    for key, val in kwargs.items():
                        if "." in key:
                            # Handle nested key in kwargs
                            nested_path_parts = key.split(".")
                            if not self._check_nested_path(
                                record, nested_path_parts, val
                            ):
                                match = False
                                break
                        elif record.get(key) != val:
                            match = False
                            break

                    if match:
                        results.append(record)

        # Case 2 & 3: Using field-value pairs
        else:
            for record in data:
                match = True

                # Handle any positional args as path-value pairs
                for i in range(0, len(args), 2):
                    if i + 1 < len(args):
                        path = args[i]
                        value = args[i + 1]
                        path_parts = path.split(".")

                        if not self._check_nested_path(record, path_parts, value):
                            match = False
                            break

                # Check keyword arguments
                for key, value in kwargs.items():
                    if "." in key:
                        # Handle nested key in kwargs
                        path_parts = key.split(".")
                        if not self._check_nested_path(record, path_parts, value):
                            match = False
                            break
                    elif record.get(key) != value:
                        match = False
                        break

                if match:
                    results.append(record)

        return results

    def _check_nested_path(
        self, record: Dict[str, Any], path_parts: List[str], value: Any
    ) -> bool:
        """
        Check if a nested path in a record matches a specific value.

        Args:
            record: The record to check
            path_parts: List of keys forming the path to the nested field
            value: Value to match

        Returns:
            True if the path matches the value, False otherwise
        """
        current = record

        for part in path_parts:
            if isinstance(current, list) and part.isdigit():
                idx = int(part)
                if idx < len(current):
                    current = current[idx]
                else:
                    return False
            elif isinstance(current, dict) and part in current:
                current = current[part]
            else:
                return False

        return current == value
