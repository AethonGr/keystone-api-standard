from enum import Enum

from pydantic import BaseModel


class HandleBaseModel(BaseModel):
    """
    Base class to handle serialization of enums and nested models to strings.
    This class extends the BaseModel from Pydantic and overrides the model_dump method
    to ensure that enums and nested models are converted to their string representations
    when the model is serialized.
    """

    def model_dump(self, **kwargs):
        """
        Override the model_dump method to convert enums and nested models to strings for serialization.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            dict: A dictionary representation of the model with enums converted to strings.
        """
        # Call the original model_dump method to get the data
        data = super().model_dump(**kwargs)

        # Recursively process the data
        def process_value(value):
            """
            Recursively process values to convert enums and nested models.

            Args:
                value: The value to process.

            Returns:
                The processed value.
            """
            if isinstance(value, Enum):
                return value.value  # Convert enum to its value
            elif isinstance(value, list):
                return [process_value(v) for v in value]  # Process list elements
            elif isinstance(value, dict):
                return {k: process_value(v) for k, v in value.items()}  # Process dict
            elif isinstance(value, BaseModel):
                return value.model_dump()  # Process nested models
            return value  # Return value as is if no processing needed

        # Apply processing to all items in the data
        return {key: process_value(value) for key, value in data.items()}
